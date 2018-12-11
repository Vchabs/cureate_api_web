from rest_framework import viewsets
from .serializers import ContentSerializer

from django.contrib.auth.mixins import LoginRequiredMixin

# from .filters import ContentFilterSet
from .models import Content
from .forms import ContentModelForm
from demographics.models import AgeLevel, Gender,Race, ReadingLevel, SmokingStatus,AlcoholStatus,ActivityLevel
from diseases.models import Disease, Complication

from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView

from users.models import User

from django.conf import settings
from django.http import HttpResponse

from psycopg2.extras import NumericRange
from datetime import timezone,datetime


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
                "activity_level":user.activity_level,
                "share_period__start_date_interval__lte": datetime.now(timezone.utc) - user.diagnosis_date, # TODO check the timezones piece 
                "share_period__end_date_interval__gte": datetime.now(timezone.utc) - user.diagnosis_date # TODO check the timezones piece 
                }
        
        return Content.objects.filter(**kwargs)

class ContentDetailView(DetailView):
    model = Content
    template_name = "content_detail.html"


class ContentFormView(FormView):
    template_name = 'form.html'
    form_class = ContentModelForm
    success_url = '/content/success/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        form.save()
        return super().form_valid(form)

class ContentFormSuccessView(TemplateView):
    model = Content
    template_name = "content_form_success.html"

def acme_challenge(request):
    return HttpResponse(settings.ACME_CHALLENGE_CONTENT)


