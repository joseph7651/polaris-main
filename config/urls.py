"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import signup_view, home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # 👈 Homepage
    path('accounts/signup/', signup_view, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('insights.urls')),
]

# touched on 2025-05-27T15:28:48.234368Z
# touched on 2025-08-14T21:16:30.689441Z
# touched on 2025-08-14T21:17:04.785200Z
# touched on 2025-08-14T21:17:15.739192Z
# touched on 2025-08-14T21:17:20.133842Z
# touched on 2025-08-14T21:17:32.683413Z
# touched on 2025-08-14T21:17:41.250128Z
# touched on 2025-08-14T21:17:49.482677Z
# touched on 2025-08-14T21:18:04.010315Z
# touched on 2025-08-14T21:18:06.133796Z
# touched on 2025-08-14T21:18:14.391814Z
# touched on 2025-08-14T21:18:16.428349Z
# touched on 2025-08-14T21:18:35.012160Z
# touched on 2025-08-14T21:18:47.410148Z
# touched on 2025-08-14T21:19:06.428408Z
# touched on 2025-08-14T21:19:17.131716Z
# touched on 2025-08-14T21:19:21.325216Z
# touched on 2025-08-14T21:19:29.505663Z
# touched on 2025-08-14T21:19:51.317443Z
# touched on 2025-08-14T21:20:04.567942Z
# touched on 2025-08-14T21:20:11.101738Z
# touched on 2025-08-14T21:20:33.002717Z
# touched on 2025-08-14T21:20:52.146538Z