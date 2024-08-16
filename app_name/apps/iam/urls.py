from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetConfirmView,
    PasswordResetView,
)
from django.conf import settings
from django.urls import include, path

urlpatterns = [
    path("login", LoginView.as_view(), name="rest_login"),
    path("logout", LogoutView.as_view(), name="rest_logout"),
]

if settings.IAM_TYPE == "BASIC":
    urlpatterns += [
        path("register", RegisterView.as_view(), name="rest_register"),
        path(
            "password/reset",
            PasswordResetView.as_view(),
            name="rest_password_reset",
        ),
        path(
            "password/reset/confirm",
            PasswordResetConfirmView.as_view(),
            name="rest_password_reset_confirm",
        ),
        path(
            "password/change",
            PasswordChangeView.as_view(),
            name="rest_password_change",
        ),
    ]
