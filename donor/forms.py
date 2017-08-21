from django import forms
from django.contrib.auth.models import User
from donor.models import DonorProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class DonorProfileForm(forms.ModelForm):
    class Meta:
        model = DonorProfile
        fields = ('picture',)