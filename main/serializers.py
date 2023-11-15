from rest_framework import serializers
from . import models as m
from django.contrib.auth.models import User




class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Status
        fields = '__all__'