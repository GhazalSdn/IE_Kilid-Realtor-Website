from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from homes.models import Housing, kilidUser
# from homes.forms import RegistrationForm

import datetime
# Create your views here.
def home(request):
    return render(request, 'index.html')
def loginSignup(request):
    return render(request, 'loginSignup.html')
def login(request):
    return render(request, 'login.html')
def signup(request):
    return render(request, 'signup.html')

def occasion(request):
    return render(request, 'occasion.html')
def user(request):
    return render(request, 'normalUser.html')
def addHousing(request):
    data = request.POST.copy()
    title = data.get('hometitle')
    price = data.get('homeprice')
    type = data.get('hometype')
    area = data.get('homearea')
    bedrooms = data.get('homebedrooms')
    parkings = data.get('homeparkings')
    locality = data.get('homelocality')
    pic = data.get('homepic')
    star = data.get('homestar')
    curr_time = datetime.datetime.now()
    housing = Housing(title=title, price=price, type=type, area=area, bedrooms=bedrooms, parkings=parkings, locality=locality, created_at=curr_time, pic=pic, star= star, estate='estate' )
    housing.save()
    return render(request, 'index.html')

def registration_view (request):
    data = request.POST.copy()
    username = data.get('username')
    name = data.get('name')
    surname = data.get('surname')
    email= data.get('email')
    password = data.get('password')
    user = kilidUser.objects.create_user(username, email, password)

    #         account = authenticate(email = email, raw_password= raw_password)
    #         login(request, account)
    #
    #         username = data.get('name')
    #         email = data.get('email')
    #         password = data.get('password')
    #         kilidU = kilidUser(username=username, price=price, password=password, email=email,userLevel=False)
    #         kilidU.save()
    #
    #         return redirect('user')
    #
    #
    # return render(request, 'loginSignup.html', {'form': RegistrationForm})










