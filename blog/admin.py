# This is where we register our models so they can show up on the admin page

from django.contrib import admin

from .models import Post

admin.site.register(Post)
