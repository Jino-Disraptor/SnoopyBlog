# This page is for the content that will be displayed on a page

from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


# To reference page you have to first specify the directory and then page name inside templates
def home(request):
    # the context lets us create a dictonary and then map our data, doesn't have to be named context but is an ideal name
    # So if we had a blog post that we are getting and we wanted to capture that information from a db and display it we do it like this
    # You also have access to the keys in the dictonary this way
    context = {"posts": Post.objects.all()}
    # we can render the context on our page by adding it to the render arguments
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "about"})


# This is using a class based view, which provides more functionality than a function based view. This view shows a list of posts
# In this class view we specify the model, we specify which template our route should look for
# we specify the context object name to be posts since that is what we have defined in home.html
# when using class based views Django has an expected way of how they should be configured, that's why we add these additional features to tell it how we have configured our page and how it should look for it
# It is not neccessary to use a classed based view, or set it up like this, it is a matter of preference
# Doing it like this is for eductational purposes. In an actual project you should stick to one way of doing things to create uniformity
class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]


# This is another class based view, this shows one specific post
# With this view we have decided to stick to Django's expected conventions
# As a result we can see that it is a lot more straight forward to create the view and all we need to specify is the model
# Django will then look for a template that matches this view and that template should be named post_detail.html which is what Django is already expecting and looks for
class PostDetailView(DetailView):
    model = Post


# We use the login required mixin to only allow logged in users to create a post
# We can't use the login decorator on classed based views
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]

    # This function overrides the default requirements of the form being that it must have an author which is required for the post model but we don't have an author field
    # It would not make sense to have an author field as a logged in user shouldn't have to fill in that field
    # We get around this by making this function that gets the logged in user as the user and submits the form with the user as the author which is what we want
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # This function makes sure that a user can only update a post that belongs to them
    # We use the UserPassesTestMixin for this
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True

        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True

        return False
