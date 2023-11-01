from rest_framework import status  # noqa: F401
from rest_framework.decorators import action  # noqa: F401
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response  # noqa: F401
from rest_framework.viewsets import ModelViewSet
from djoser.compat import get_user_email
from djoser.views import UserViewSet as DjoserUserViewSet


from .serializers import (
    UserSerializer,
    InviteUserSerializer,
    ProfileSerializer,
)

from apps.authentication.models import User, Profile

class UserViewset(DjoserUserViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        """remove require auth permission on invited user activation view."""
        if self.action == "invitation":
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def get_instance(self):
        return self.request.user

    def get_serializer_class(self):
        if self.action == "invitation":
            return InviteUserSerializer
        return super().get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True
        return super().get_serializer(*args, **kwargs)

    @action(methods=["POST"], detail=False)
    def invitation(self, request, *args, **kwargs):
        """
        send an invitation email to a user or group of users
        """

        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


class UserProfileViewset(ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


# class UserSettingsViewset(ModelViewSet):
#     serializer_class = SettingSerializer
#     queryset = Settings.objects.all()
