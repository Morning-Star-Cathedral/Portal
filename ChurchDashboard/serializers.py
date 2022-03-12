from rest_framework import serializers
from .models import *

class DbUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = DBUser
        fields = (
        'title', 'name','chapel','group','email',
               )


class MemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Members
        fields = ('title', 'first_name', 'other_name', 'last_name','sex','chapel', 'group', 'dob', 'phone_number',
                  'whatsapp_number','other_phone_number','area_of_residence','gps_address',)


class ChapelDbuserSerializer(serializers.ModelSerializer):
    mem = MemSerializer(many=True, read_only=True)

    class Meta:
        model = Chapels
        fields = ('name', 'mem')

