from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'sex', 'age', 'about_me', 'profile_picture', 'cover_picture']
