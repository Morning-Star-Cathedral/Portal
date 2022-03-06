from django.urls import path
from ChurchDashboard.views import  *
urlpatterns = [
    path('',list_view_member, name='list_member_url'),
    path('attendances/', list_view_attendance, name = 'list_attendance_url'),
    path('att_summ/',attendance_summmaries_list, name = 'list_summary_attendance_url'),
    path('groups/',groups_list, name = 'list_group_url'),
    path('chapels/',chapel_list, name ='list_chapel_url'),
    path('grouplead/',db_user_list, name='list_group_url'),


]
