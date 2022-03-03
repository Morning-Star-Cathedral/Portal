from django.urls import path
from ChurchDashboard.views import  list_view_member, list_view_attendance

urlpatterns = [
    path('',list_view_member, name='List_Member'),
    path('attendances/', list_view_attendance, name = 'List_Attendance'),


]
