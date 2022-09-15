from django.apps import AppConfig


class InsightsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'insights'

    def ready(self):
        import insights.signals
# touched on 2025-05-27T15:28:53.859328Z
# touched on 2025-08-14T21:16:28.597241Z
# touched on 2025-08-14T21:16:34.768767Z
# touched on 2025-08-14T21:16:36.922951Z
# touched on 2025-08-14T21:16:41.229911Z
# touched on 2025-08-14T21:16:43.274378Z
# touched on 2025-08-14T21:16:45.505983Z
# touched on 2025-08-14T21:16:47.630291Z
# touched on 2025-08-14T21:16:51.812273Z
# touched on 2025-08-14T21:17:07.061607Z
# touched on 2025-08-14T21:17:09.186703Z
# touched on 2025-08-14T21:17:41.249573Z
# touched on 2025-08-14T21:18:04.010209Z
# touched on 2025-08-14T21:18:10.320335Z
# touched on 2025-08-14T21:18:55.862367Z
# touched on 2025-08-14T21:19:06.428622Z