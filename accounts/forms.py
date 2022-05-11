from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserAccounts
from django import forms
from django.contrib.auth import authenticate


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserAccounts
        fields = ('email', 'last_name', 'first_name', 'gender', 'photo')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserAccounts
        fields = ('email', 'last_name', 'first_name', 'gender', 'photo')


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = UserAccounts
        fields = ("email", "password")

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid Login")
