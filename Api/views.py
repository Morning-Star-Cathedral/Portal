from django.shortcuts import render
from ChurchDashboard.models import *
from rest_framework import generics
from Api.serializers import DbUserSerializer, ChapelDbuserSerializer, GroupSerializer, ChapelMemberSerializer, \
    MemberAttendanceSerializer



# API VIEWS
# uSER lIST API
class DbUserListAPi(generics.ListAPIView):
    queryset = DBUser.objects.all()
    serializer_class = DbUserSerializer


# CHAPEL LIST apI
class ChapelListAPi(generics.ListAPIView):
    queryset = Chapels.objects.all()
    serializer_class = ChapelDbuserSerializer


class GroupsApi(generics.ListAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupSerializer


class ChapelMemberListAPI(generics.ListAPIView):
    queryset = Chapels.objects.all()
    serializer_class = ChapelMemberSerializer


class AttendanceMemberListAPi(generics.ListAPIView):
    queryset = Attendances.objects.all().order_by('service_date')
    serializer_class = MemberAttendanceSerializer
