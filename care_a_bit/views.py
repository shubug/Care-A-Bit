from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from ngo.models import NgoCategory

def index(request):
    #return HttpResponse("First attempt from Care A Bit")
    ngo_cats = NgoCategory.objects.order_by('-num_of_contrib')[:3]
    context_dict = {'boldmessage': "Call for Care A Bit", 'categories': ngo_cats}
    return render(request, 'home/index.html', context_dict)