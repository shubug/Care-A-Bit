from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from donor.forms import UserForm, DonorProfileForm
from django.contrib.auth import authenticate, login
from ngo.models import NgoCategory
from helpers.email import send_emailtemplate
from django.core.mail import send_mail
from django.conf import settings
# from helpers.utils import flush_cache

def donor(request):
    return render(request, 'donor/firstpage.html', {})

def signup(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = DonorProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()
             
            print user.email
            send_mail("Successful registeration on Care_A_bit. Fanks !!", 'contact_message', 
                               settings.EMAIL_HOST_USER,
                               [user.email], fail_silently = False) 

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
            # return render(request, 'home/index.html', {}) In case we want user go to homepage directly
        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = DonorProfileForm()

    return render(request,
            'donor/signup.html',
            {'user_form': user_form, 'donor_profile_form': profile_form, 'registered': registered} )

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/donor/')
            else:
                return HttpResponse("Sorry Your account is disabled.")
                #send_emailtemplate to ask user to re-activate his/her account
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'donor/login.html', {})

