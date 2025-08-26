from django.apps import AppConfig


class AppAuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.app_auth'
    def ready(self):
        import core.app_auth.signals  # noqa

