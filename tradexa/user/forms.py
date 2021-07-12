from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from.models import Post
from django.forms import ModelForm



 
class SignUpForm(UserCreationForm):
  
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}



class PostForm(ModelForm):
    class Meta:
        model=Post
        fields=['username','text']