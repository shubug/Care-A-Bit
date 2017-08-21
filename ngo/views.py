from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# from donor.forms import UserForm, DonorProfileForm
from django.contrib.auth import authenticate, login
from ngo.models import NgoCategory, Ngo

def ngo(request):
	return HttpResponse("This is a demo Ngo page which hasn't been designed yet !!")

def category(request, category_name_slug):
    context_dict = {}
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = NgoCategory.objects.get(slug=category_name_slug)
        context_dict['category_domain'] = category.domain

        # Note that filter returns >= 1 model instance.
        ngos = Ngo.objects.filter(category=category)
        context_dict['ngos'] = ngos
        context_dict['category'] = category
    except NgoCategory.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    return render(request, 'ngo/category.html', context_dict)
