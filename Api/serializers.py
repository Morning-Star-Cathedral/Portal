from rest_framework import serializers
from ChurchDashboard.models import *


class MemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ('title', 'first_name', 'other_name', 'last_name', 'sex', 'chapel', 'group', 'dob', 'phone_number',
                  'whatsapp_number', 'other_phone_number', 'area_of_residence', 'gps_address',)


class GroupSerializer(serializers.ModelSerializer):
    group_members = MemSerializer(many=True, read_only=True)

    class Meta:
        model = Groups
        fields = ('name', 'group_members',)


class DbUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DBUser
        fields = (
            'title', 'name', 'chapel', 'group', 'email',
        )


class ChapelDbuserSerializer(serializers.ModelSerializer):
    user_chapel = DbUserSerializer(many=True, read_only=True)

    class Meta:
        model = Chapels
        fields = ('id', 'name', 'user_chapel')


class ChapelMemberSerializer(serializers.ModelSerializer):
    chapel_members = MemSerializer(many=True, read_only=True)

    class Meta:
        model = Chapels
        fields = ('id', 'name', 'chapel_members')


class MemberAttendanceSerializer(serializers.ModelSerializer):
    members_attendance = MemSerializer(many=True, read_only=True)

    class Meta:
        model =Attendances
        fields = ('id', 'service_date', 'is_present', 'reason', 'comment', 'completed', 'members_attendance',)

