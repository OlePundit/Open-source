import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from model_utils import Choices
from model_utils.fields import StatusField
from model_utils.models import SoftDeletableModel, TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField

from apps.authentication.managers import UserManager


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f"users/user-{instance.id}/{filename}"


# TODO: ADD DJANGO GUARDIAN FOR PERMISSION / ANY RELEVANT 3RD PARTY APP
class User(AbstractUser, TimeStampedModel, SoftDeletableModel):
    """
    Default custom user model.
    """

    USER_TYPE = Choices("user", "creator")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(_("User Name"), blank=True, max_length=255)
    first_name = models.CharField(_("First Name"), blank=True, max_length=255)
    last_name = models.CharField(_("Last Name"), blank=True, max_length=255)
    email = models.EmailField(_("Email address"), unique=True)
    type = StatusField(_("User Type"), choices_name="USER_TYPE", default="user")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self) -> str:
        return self.email


class Profile(TimeStampedModel, SoftDeletableModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone_number = PhoneNumberField(_("User's Phone Number"), blank=True)
    avatar = ProcessedImageField(
        upload_to=user_directory_path,
        processors=[ResizeToFill(200, 200)],
        blank=True,
        null=True,
        format="JPEG",
        options={"quality": 80},
    )
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self) -> str:
        return self.user.email


# class Settings(TimeStampedModel):
#     THEMES = Choices("dark", "light")
#     LAYOUT = Choices("sidenav", "topnav")

#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="settings")
#     theme = StatusField(_("Preffered Theme"), choices_name="THEMES", default="dark")
#     layout = StatusField(_("Preffered Layout"), choices_name="LAYOUT", default="sidenav")

#     class Meta:
#         verbose_name = "User Setting"
#         verbose_name_plural = "User Settings"

#     def __str__(self) -> str:
#         return self.user.email
