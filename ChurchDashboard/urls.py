from django.urls import path
from ChurchDashboard.views import  list_view_member, list_view_attendance,attendance_summmaries_list

urlpatterns = [
    path('',list_view_member, name='List_Member'),
    path('attendances/', list_view_attendance, name = 'List_Attendance'),
    path('att_summ/',attendance_summmaries_list, name = 'Summary_attendance'),


]
