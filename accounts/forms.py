from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserAccounts
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserAccounts
        fields = ('email', 'last_name', 'first_name', 'gender', 'photo')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserAccounts
        fields = ('email',  'last_name', 'first_name', 'gender', 'photo')


#
# class SignupForm(forms.ModelForm):
#     """user signup form"""
#     password = forms.CharField(widget=forms.PasswordInput())
#
#     class Meta:
#         model = get_user_model()
#         fields = ('email', 'name', 'password',)

#
# class LoginForm(forms.Form):
#     """user login form"""
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput())
