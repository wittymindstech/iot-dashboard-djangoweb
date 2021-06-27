from msilib.schema import ListView

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Profile, IOTDevice
from django.contrib.auth.models import User
from django.contrib import messages


def register(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            if User.objects.filter(username__iexact=username).exists():
                messages.error(request, "Username is taken")
                return render(request, "auth/sign-up.html", )
            if User.objects.filter(email__iexact=email).exists():
                messages.error(request, "Email id already in use.")
                return render(request, "auth/sign-up.html", )
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            Profile.objects.create(user=user)
            messages.success(request, "Sign Up Successfull! ")
            return redirect('login')
        elif request.method == "GET":
            return render(request, "auth/sign-up.html", )
        else:
            return render(request, "auth/sign-up.html", )
    except:
        messages.error(request, "Something went wrong. Please try again.")
        return render(request, "auth/sign-up.html", )


def login_view(request):
    # form = LoginForm(request.POST or None)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password, end="\n\n", sep=" | ")
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                messages.success(request, "Sign in Successful.")
                return redirect('/index')
            messages.success(request, "Sign in Successful.")
            return redirect("/index")

        else:
            messages.error(request, "Username or Password Doesn't match")
            return render(request, "auth/sign-in.html", )
    elif request.method == "GET":
        return render(request, "auth/sign-in.html", )
    else:
        messages.error(request, "Error validating the form")
        return render(request, "auth/sign-in.html", )


@login_required
def index(request):
    portfolio_list = IOTDevice.objects.all().order_by('-created_date')
    print(portfolio_list)
    context = {
        "portfolios": portfolio_list,
    }
    return render(request, "index.html", context)


@login_required
def addDevice(request):
    if request.method == "POST":
        device_name = request.POST.get("device_name")
        registration_number = request.POST.get("registration_number")
        city = request.POST.get("city")
        IOTRecord = IOTDevice.objects.create(device_name=device_name, city=city,
                                             registration_number=registration_number)
        print('Successfully Created')
        IOTRecord.save()
        return HttpResponseRedirect(reverse('addDevice'))
    return render(request, "device-upload.html")


def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        try:
            status = IOTDevice.objects.filter(
                Q(device_name__icontains=query) | Q(city__icontains=query) | Q(registration_number__icontains=query))
        except:
            return render(request, "search.html", {'books': status})
        context = {
            'all_search_results': status,
        }
        return render(request, "search.html", context)
    else:
        return render(request, "search.html", context='Not Found')
