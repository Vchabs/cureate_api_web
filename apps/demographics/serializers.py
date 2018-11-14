
from rest_framework import serializers

from .models import ReadingLevel, Race, AgeLevel, Gender, SmokingStatus, AlcoholStatus, ActivityLevel

class AgeLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeLevel
        fields = ['ID','value']


class ReadingLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingLevel
        fields = ['ID','value']


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = ['ID','value']


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ['ID','value']


class SmokingStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmokingStatus
        fields = ['ID','value']


class AlcoholStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlcoholStatus
        fields = ['ID','value']
        

class ActivityLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityLevel
        fields = ['ID','value']