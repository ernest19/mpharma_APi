from django.contrib.auth.models import User, Group

from rest_framework import serializers

from apiApp.models import IcdCode



class IcdcodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IcdCode
        fields = ('category_code', 'diagnosis_code', 'full_code', 'abbreviated_description', 'full_description', 'category_title')
