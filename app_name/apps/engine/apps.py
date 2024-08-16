from django.apps import AppConfig


class EngineConfig(AppConfig):
    name = "app_name.apps.engine"

    def ready(self) -> None:
        """Overwrite if needed"""
        return super().ready()
