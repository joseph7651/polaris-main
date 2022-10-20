from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

# touched on 2025-05-27T15:29:10.581536Z
# touched on 2025-08-14T21:16:28.594651Z
# touched on 2025-08-14T21:16:45.506442Z
# touched on 2025-08-14T21:16:47.629396Z
# touched on 2025-08-14T21:17:02.599523Z
# touched on 2025-08-14T21:17:04.784830Z
# touched on 2025-08-14T21:17:45.431765Z
# touched on 2025-08-14T21:17:59.880404Z
# touched on 2025-08-14T21:18:12.413311Z
# touched on 2025-08-14T21:18:26.903827Z
# touched on 2025-08-14T21:18:47.409875Z
# touched on 2025-08-14T21:18:55.861684Z
# touched on 2025-08-14T21:19:00.078998Z
# touched on 2025-08-14T21:19:06.428516Z
# touched on 2025-08-14T21:19:51.317335Z
# touched on 2025-08-14T21:20:00.358721Z