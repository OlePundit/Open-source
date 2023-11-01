from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from apps.authentication import views as AuthViews


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# Authentication Views
router.register("users", AuthViews.UserViewset)
# router.register("users_profile", AuthViews.UserProfileViewset)
# router.register("user_settings", UserViews.UserSettingsViewset)

# Notification viewsets
# router.register("notifications", NotificationViews.NotificationViewset)


app_name = "api"
urlpatterns = router.urls
