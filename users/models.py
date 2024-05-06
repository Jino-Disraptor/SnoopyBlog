from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# By default django doesn't provide profile picture field and others
# We can create another model that has a relationship to our user model, in this case we are creating a profile model that has a relationship to the User model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default="default.jpg", upload_to="profile_pics"
    )  # default is a default image that will apply to all users that register, upload_to is the directory the pictures are saved


# This method is to display our content in a specific way that we want


def __str__(self):
    return f"{self.user.username} Profile"


# THis is to resize images to a specified size
# def save(self, *args, **kwargs):

#     super().save(*args, **kwargs)

#     img = Image.open(self.image.path)

#     if img.height > 300 or img.width > 300:
#         output_size = (300, 300)
#         img.thumbnail(output_size)
#         img.save(self.image.path)
