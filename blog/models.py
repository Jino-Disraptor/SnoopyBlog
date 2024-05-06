# This page is where we create our database models
# databases are defined as class and inaide the class we list all the fields we want in our table
# whenever you make a change to the database or add a new model you need to run python manage.py makemigrations
# To view SQl that is executed when running python manage.py makemigrations then run python manage.py sqlmigrate app_name migration_number, you will get these values from the terminal after you have ran python manage.py makemigrations
# migrations are useful because they allow us to make changes to our db easily even if we've added data or removed data
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # This makes sure that when a user is deleted then their posts are also delted but if a post is deleted then the user still remains

    # This method returns the blog and title of the blog
    def __str__(self):
        return self.title

    # In order for django to redirect us to a page after we have created a new blog we use the reverse method
    # this will return the url in the form of a string and then we can use the redirect method in views.py to redirect to that url
    # we don't use redirect method here as this page is not meant for routing
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
