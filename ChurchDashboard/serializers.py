from rest_framework import serializers
from .models import *

class DbUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = DBUser
        fields = (
        'title', 'name','chapel','group','email',
               )



class ChapelDbuserSerializer(serializers.ModelSerializer):
    db_user = DbUserSerializer(many=True, read_only=True)

    class Meta:
        model = Chapels
        fields = ('name', 'db_user',)

