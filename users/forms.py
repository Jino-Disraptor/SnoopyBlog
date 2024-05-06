# This page is manually created
# This pages allows us to create forms which inherit from UserCreationForm so that we can add our own fields (we did not create the user creation form)

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# add email input to UserCreationForm
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # This gives us a nested namespace for configs in one place, it says the model that is affected is the user and when saved it will save to the user model with the fields specified
    # when a post request is made on a form which is handled in views.py it is able to store that info in the relevant db as we have specified which model the form acts on
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# create a model form that will work with a specific database


# This form lets the user update the user details
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]


# This form lets the user update the profile picture
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]
