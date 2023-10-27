from rest_framework import serializers
from .models import *

class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creators
        fields = ['name', 'email','password']