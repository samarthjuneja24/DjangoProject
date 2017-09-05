from django import forms
from .models import UserProfile,Video
from django.contrib.auth.models import User
from django.forms import ModelForm
class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['first_name','last_name','username','password','email']
        #fields='__all__'

class ProfilePicForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['profile_pic']

class VideoForm(forms.ModelForm):
    class Meta:
        model=Video
        fields=['username','videotitle']
