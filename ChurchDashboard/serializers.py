from rest_framework import serializers
from .models import *

class DbUserSerializer(serializers.ModelSerialier):
    model = DBUser
    fields = (
        'title', 'name','chapel','group','email',
    )



class ChapelDbuserSerializer(serializers.ModelSerialier):
    db_user = DbUserSerializer(many=True, read_only=True)

    class Meta:
        model = Chapels
        fields = ('name', 'db_user',)

