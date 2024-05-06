# create this page manually as it is not created by default
# This page is used to handle routes for an app belonging to this module
# These urls need to be referenced in the project's url i.e (Snoopy_Blog URLS)

from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="blog-home"),
    # This is a different way of configuring a URL, it is not neccesaary to configure it like this
    # The benefits of this way is that it gives us the functionality of loading a specific blog post using the primapry key
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("about/", views.about, name="blog-about"),
]
