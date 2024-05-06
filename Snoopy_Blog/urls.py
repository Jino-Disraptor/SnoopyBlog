"""
URL configuration for Snoopy_Blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static


# This is the main route page for the project
# Add routes from other apps, you only need to specify the folder name as it will then search that folder's
# URL page for any routes that match ie(it checks blog folder urls page and checks all those routes)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", user_views.register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="users/login.html"
        ),  # we don't need to create a view for this as this login view is built in and we can just specify where this page must be found
        name="login",
    ),
    path(
        "logout/",
        user_views.logout_view,  # we have to create a logout view and then reference the view here
        name="logout",
    ),
    path("profile/", user_views.profile, name="profile"),
    path("", include("blog.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
