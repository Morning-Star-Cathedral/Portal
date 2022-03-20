from django.urls import path
from .views import *
# from rest_framework_swagger.views import get_swagger_view

# schema_view = get_swagger_view(title='Church Dashboard API')

urlpatterns = [
    # path('', schema_view),
    path('zzdbuserzz/', DbUserListAPi.as_view()),
    path('amchapszzz/', ChapelListAPi.as_view(), name='CHAPEL_LIST_API'),
    path('livedgroupzz/', GroupsApi.as_view()),
    path('zzchapelmembers/', ChapelMemberListAPI.as_view()),
    path('attsmemes/', AttendanceMemberListAPi.as_view()),


]