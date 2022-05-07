from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import UserAccounts
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *
from django.contrib.auth.models import Group

admin.site.site_header = "CTAC PastCare admin"
admin.site.site_title = "CTAC PastCare admin site"
admin.site.index_title = "CTAC PastCare admin"

admin.site.unregister(Group)

class CTACAdminArea(admin.AdminSite):
    site_header = "CTAC PastCare admin"

# Register your models here.
@admin.register(UserAccounts)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = UserAccounts
    list_display = ('email',  'is_staff', 'is_active', 'image_tag')
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email',  'last_name', 'first_name', 'gender',
                           'photo', 'password',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email',  'last_name', 'first_name', 'gender',
                       'photo', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


@admin.register(DBUser)
class DBUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'chapel', 'group']
    fields = ['title', 'name', 'email', 'chapel', 'group']
    search_fields = ['name']


@admin.register(Chapels)
class ChapelsAdmin(admin.ModelAdmin):
    fields = ['name']
    search_fields = ['name']


@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    fields = ['name']
    search_fields = ['name']


@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number', 'group', ]
    list_filter = ['group', ]
    search_fields = ['phone_number', 'last_name', 'first_name']


@admin.register(RoleUser)
class RoleUserAdmin(admin.ModelAdmin):
    list_display = ['role', 'user']


@admin.register(Attendances)
class AttendancesAdmin(admin.ModelAdmin):
    list_display = [ 'service_date', 'is_present']
    search_fields = ['service_date', 'member']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(AttendanceSummaries)
class AttendanceSummariesAdmin(admin.ModelAdmin):
    list_display = ['weekday', 'attendance_date', 'group', 'total_present']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
