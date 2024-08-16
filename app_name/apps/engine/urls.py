from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=False)

router.register(prefix="users", viewset=views.UserViewSet)


urlpatterns = [
    # documentation for API
    path(
        "api/schema",
        view=SpectacularAPIView.as_view(api_version=settings.API_VERSION),
        name="schema",
    ),
    path(
        "api/swagger/",
        view=SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger",
    ),
    path(
        "api/redoc/",
        view=SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    # entry point for API
    path("api/", include(router.urls)),
    # path("api/", include("app_name.apps.iam.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
