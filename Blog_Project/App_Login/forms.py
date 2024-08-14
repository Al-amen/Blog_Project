from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from App_Login import models
class SignUpForm(UserCreationForm):
    
    email = forms.EmailField(label="Email address" , required=True)
    
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class UserProfileChange(UserChangeForm):
    
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')
    
class ProfilePic(forms.ModelForm):
        class Meta:
            model = models.UserProfile
            fields = ['profile_pic',]