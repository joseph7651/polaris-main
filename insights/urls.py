from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_redirect, name='dashboard_redirect'),
    path('dashboard/internal/', views.internal_dashboard, name='internal_dashboard'),
    path('dashboard/client/', views.client_dashboard, name='client_dashboard'),
    path('generate-assessment/', views.generate_assessment, name='generate_assessment'),
    path('api/pillar-score-trends/', views.pillar_score_trends_api, name='pillar_score_trends_api'),
]

# touched on 2025-05-27T15:29:02.325030Z
# touched on 2025-05-27T15:45:56.087430Z
# touched on 2025-08-14T21:16:45.506139Z
# touched on 2025-08-14T21:16:55.963594Z
# touched on 2025-08-14T21:17:04.786246Z
# touched on 2025-08-14T21:17:26.437381Z
# touched on 2025-08-14T21:17:30.625597Z
# touched on 2025-08-14T21:17:41.249906Z
# touched on 2025-08-14T21:18:20.559715Z
# touched on 2025-08-14T21:18:30.913357Z
# touched on 2025-08-14T21:18:47.410061Z
# touched on 2025-08-14T21:19:10.595303Z
# touched on 2025-08-14T21:19:12.729094Z
# touched on 2025-08-14T21:19:15.008109Z
# touched on 2025-08-14T21:19:23.467191Z
# touched on 2025-08-14T21:19:42.235852Z
# touched on 2025-08-14T21:20:11.101650Z
# touched on 2025-08-14T21:20:20.209347Z
# touched on 2025-08-14T21:20:24.750511Z
# touched on 2025-08-14T21:20:35.063600Z
# touched on 2025-08-14T21:20:37.214481Z
# touched on 2025-08-14T21:20:43.559998Z