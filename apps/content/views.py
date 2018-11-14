from rest_framework import viewsets
from .serializers import ContentSerializer
# from .filters import ContentFilterSet
from .models import Content
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


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
    template_name = 'home.html'

    def get_queryset(self):
    	user = self.request.user
    	print("hello")

    	return Content.objects.filter(user_id = user)