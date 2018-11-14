from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.http import HttpResponseNotFound
from django.contrib.auth import authenticate, login

from django.shortcuts import render_to_response

def index (request):
    return render_to_response('app/index.html')

#Quick home page
class Home(TemplateView):
    template_name = "home.html"


# def login_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect('/content/list_view')
#     else:
#     	return render_to_response('404.html')


# def logout_view(request):
#    	logout(request)
#    	return render_to_response('registration/logout.html')