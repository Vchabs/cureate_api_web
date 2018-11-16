"""

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from main.views import Home
from content.views import ContentListView


api_urls = [
url(r'^api/v1.0/content/',include('content.api_urls')),
url(r'^api/v1.0/demographics/',include('demographics.api_urls'))
]


urlpatterns = [
    # url(r'^login/$', main.views.login, {"template_name" : "registration/login.html"}, name='login'),
    # url(r'^logout/$', main.views.logout, {"template_name" : "registration/logout.html"}, name='logout'),

    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
    # url(r'^$',ContentListView.as_view(),name='home'),
    url(r'testContent/',ContentListView.as_view()),

]
urlpatterns+=api_urls