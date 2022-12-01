from django.http import HttpResponseForbidden

def role_required(required_role):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if hasattr(request.user, 'userprofile') and request.user.userprofile.role == required_role:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("⛔ You are not authorized to access this page.")
        return _wrapped_view
    return decorator

# touched on 2025-05-27T15:28:56.617211Z
# touched on 2025-05-27T15:29:05.129847Z
# touched on 2025-08-14T21:16:41.230115Z
# touched on 2025-08-14T21:16:43.274170Z
# touched on 2025-08-14T21:17:02.598832Z
# touched on 2025-08-14T21:17:07.061495Z
# touched on 2025-08-14T21:17:55.705359Z
# touched on 2025-08-14T21:18:08.238806Z
# touched on 2025-08-14T21:18:10.319839Z
# touched on 2025-08-14T21:18:30.913473Z
# touched on 2025-08-14T21:18:41.298771Z
# touched on 2025-08-14T21:18:45.292966Z
# touched on 2025-08-14T21:18:53.713293Z
# touched on 2025-08-14T21:19:15.007999Z
# touched on 2025-08-14T21:19:17.131831Z
# touched on 2025-08-14T21:19:19.218979Z
# touched on 2025-08-14T21:19:42.236567Z
# touched on 2025-08-14T21:19:48.299318Z
# touched on 2025-08-14T21:20:24.750153Z
# touched on 2025-08-14T21:20:30.929739Z
# touched on 2025-08-14T21:21:04.682747Z
# touched on 2025-08-14T21:21:17.609411Z