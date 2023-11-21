from django.db import transaction, IntegrityError
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from rest_framework import serializers
from rest_framework.settings import api_settings
from drf_writable_nested.mixins import NestedUpdateMixin
from phonenumber_field.serializerfields import PhoneNumberField

from djoser.conf import settings as djoser_settings

from apps.authentication.models import User, Profile


class ProfileSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberField(region="KE")

    class Meta:
        model = Profile
        fields = [
            "id",
            "phone_number",
            "avatar",
        ]


class UserSerializer(NestedUpdateMixin, serializers.ModelSerializer):
    profile = ProfileSerializer(required=False, allow_null=True)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "type",
            "profile",
        ]
        read_only_fields = ("id",)


class InviteUserSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True, style={"input_type": "text"})
    last_name = serializers.CharField(required=True, style={"input_type": "text"})
    email = serializers.EmailField(required=True, style={"input_type": "email"})
    # TODO: VALIDATE FIELDS


class UserCreateMixin:
    def create(self, validated_data):
        try:
            user = self.perform_create(validated_data)
        except IntegrityError:
            self.fail("cannot_create_user")

        return user

    def perform_create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
            if djoser_settings.SEND_ACTIVATION_EMAIL:
                user.is_active = False
                user.save(update_fields=["is_active"])
        return user


class UserCreateSerializer(UserCreateMixin, serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    default_error_messages = {
        "cannot_create_user": djoser_settings.CONSTANTS.messages.CANNOT_CREATE_USER_ERROR
    }

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "type",
            "password",
        ]

    def validate(self, attrs):
        user = User(**attrs)
        password = attrs.get("password")

        try:
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"password": serializer_error[api_settings.NON_FIELD_ERRORS_KEY]}
            )

        return attrs


class UserCreatePasswordRetypeSerializer(UserCreateSerializer):
    default_error_messages = {
        "password_mismatch": djoser_settings.CONSTANTS.messages.PASSWORD_MISMATCH_ERROR
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["re_password"] = serializers.CharField(
            style={"input_type": "password"}
        )

    def validate(self, attrs):
        self.fields.pop("re_password", None)
        re_password = attrs.pop("re_password")
        attrs = super().validate(attrs)
        if attrs["password"] == re_password:
            return attrs
        else:
            self.fail("password_mismatch")
