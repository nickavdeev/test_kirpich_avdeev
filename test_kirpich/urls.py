from django.conf.urls import include
from django.contrib import admin
from django.urls import path

api_urlpatterns = [
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("menu/", include("menu.urls")),
]

urlpatterns = [
    path("api/v1/", include(api_urlpatterns)),
    path("admin/", admin.site.urls),
    path("", include("menu.urls")),
]
