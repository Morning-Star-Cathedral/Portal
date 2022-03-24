from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import UserAccounts
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm


# Register your models here.
@admin.register(UserAccounts)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = UserAccounts
    list_display = ('email', 'username', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'last_name', 'first_name', 'gender',
                           'photo', 'password',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'last_name', 'first_name', 'gender',
                       'photo', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
