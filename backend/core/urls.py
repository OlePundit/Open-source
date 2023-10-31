"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from rest_framework_simplejwt.views import token_blacklist
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # # Optional UI:
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    # path(
    #     "api/schema/redoc/",
    #     SpectacularRedocView.as_view(url_name="schema"),
    #     name="redoc",
    # ),
]


API_BASE = r"^api/v1/"
API_AUTH = r"^api/v1/auth/"

# API URLS
urlpatterns += [
    re_path(API_AUTH, include("rest_framework.urls")),
    re_path(API_AUTH, include("djoser.urls")),
    re_path(API_AUTH, include("djoser.urls.jwt")),
    re_path("api/v1/auth/jwt/destroy/", token_blacklist, name="jwt-logout"),
    # re_path(API_BASE, include("core.api_router")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
