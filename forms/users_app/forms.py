from django import forms
from .models import Profile
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["profile_picture","bio","location","birth_date"]  

    
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["last_name","email","first_name"]