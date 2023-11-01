# from axes.signals import user_locked_out
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.signals import notify
from rest_framework.exceptions import PermissionDenied

from apps.authentication.models import Profile

User = get_user_model()

WELCOME_MESSAGE = (
    "Welcome to AFroPix! We're excited to have you on board."
    "If you have any questions or feedback, don't hesitate to reach "
    "out to our support team. Happy Creating!"
)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# @receiver(post_save, sender=User)
# def create_user_settings(sender, instance, created, **kwargs):
#     if created:
#         Settings.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_settings(sender, instance, **kwargs):
#     instance.settings.save()


@receiver(post_save, sender=User)
def user_welcome_message(sender, **kwargs):
    if kwargs.get("created", False):
        instance = kwargs.get("instance")
        notify.send(instance, recipient=instance, verb=WELCOME_MESSAGE, level="success")


# # axes rate limit for DRF
# @receiver(user_locked_out)
# def raise_permission_denied(*args, **kwargs):
#     # checking the path to disable this function if request is not from DRF
#     request = kwargs.get("request")
#     if request.META["PATH_INFO"] == "/admin/login/":
#         return
#     raise PermissionDenied("Too many failed login attempts")
