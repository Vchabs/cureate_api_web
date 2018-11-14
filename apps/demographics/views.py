from rest_framework import viewsets
from .serializers import AgeLevelSerializer,ReadingLevelSerializer,RaceSerializer, GenderSerializer,SmokingStatusSerializer,ActivityLevelSerializer,AlcoholStatusSerializer
from .models import ReadingLevel, Race, AgeLevel, Gender, SmokingStatus, AlcoholStatus,ActivityLevel


class AgeLevelViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = AgeLevel.objects.only("ID","value")
    serializer_class = AgeLevelSerializer

class ReadingLevelViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = ReadingLevel.objects.only("ID","value")
    serializer_class = ReadingLevelSerializer

class RaceViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Race.objects.only("ID","value")
    serializer_class = RaceSerializer

class GenderViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Gender.objects.only("ID","value")
    serializer_class = GenderSerializer


class SmokingStatusViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = SmokingStatus.objects.only("ID","value")
    serializer_class = SmokingStatusSerializer


class AlcoholStatusViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = AlcoholStatus.objects.only("ID","value")
    serializer_class = AlcoholStatusSerializer


class ActivityLevelViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = ActivityLevel.objects.only("ID","value")
    serializer_class = ActivityLevelSerializer