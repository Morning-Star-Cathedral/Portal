from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserAccounts


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserAccounts
        fields = ('email', 'username', 'last_name', 'first_name', 'gender', 'photo')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserAccounts
        fields = ('email', 'username', 'last_name', 'first_name', 'gender', 'photo')
