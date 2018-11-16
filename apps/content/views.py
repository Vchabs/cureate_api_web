from rest_framework import viewsets
from .serializers import ContentSerializer

from django.contrib.auth.mixins import LoginRequiredMixin

# from .filters import ContentFilterSet
from .models import Content
from demographics.models import AgeLevel, Gender,Race, ReadingLevel, SmokingStatus,AlcoholStatus,ActivityLevel
from diseases.models import Disease, Complication

from django.views.generic import ListView, DetailView

from users.models import User


from psycopg2.extras import NumericRange



class ContentViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Content.objects.only("title","description")
    serializer_class = ContentSerializer
    # filter_class = ContentFilterSet


class ContentListView(LoginRequiredMixin,ListView):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    model = Content
    context_object_name = 'content_list' 

    template_name = 'content_page.html'

    def get_queryset(self):
        user = self.request.user 
        kwargs = {"gender":user.gender,
                "diseases":user.disease,
                #"complications":user.complication,
                #"race":user.race,
                # "age_level":user.age_level,
                # "reading_level":user.reading_level,
                "smoking_status":user.smoking_status,
                "alcohol_status":user.alcohol_status, 
                "activity_level":user.activity_level
                }
        
        return Content.objects.filter(**kwargs)



class ContentDetailView(DetailView):
    model = Content
    template_name = "content_detail.html"






