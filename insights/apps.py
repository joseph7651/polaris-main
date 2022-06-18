from django.apps import AppConfig


class InsightsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'insights'

    def ready(self):
        import insights.signals
# touched on 2025-05-27T15:28:53.859328Z
# touched on 2025-08-14T21:16:28.597241Z
# touched on 2025-08-14T21:16:34.768767Z