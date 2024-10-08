from django.apps import apps
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("app_name.apps.engine.urls")),
    path("admin/", admin.site.urls),
]

# if apps.is_installed("silk"):
#     urlpatterns.append(path("profiler/", include("silk.urls")))
