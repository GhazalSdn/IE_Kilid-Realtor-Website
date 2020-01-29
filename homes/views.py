from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from homes.models import Housing, kilidUser,Comment,Image
from django.contrib.auth.models import User
# from homes.forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.core import serializers
import datetime



id = 0

# Create your views here.
def home(request):
    usernameHome = False
    if request.user.is_authenticated:
        usernameHome = request.user.username
    return render(request, 'index.html',{"username": usernameHome})

def loginSignup(request):
    return render(request, 'loginSignup.html')
def login(request):
    return render(request, 'login.html')
def signup(request):
    return render(request, 'signup.html')

def occasion(request):
    return render(request, 'occasion.html')
def user(request):
    usernameHome = None
    if request.user.is_authenticated:
        usernameHome = request.user.username
    return render(request, 'normalUser.html',{'username': usernameHome})
def manager(request):
    return render(request, 'manager.html')

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
    estate = None
    if request.user.is_authenticated:
        estate = request.user.username
    housing = Housing(title=title, price=price, type=type, area=area, bedrooms=bedrooms, parkings=parkings, locality=locality, created_at=curr_time, star= star, estate=estate)
    housing.save()
    image = Image(image=pic, related_house=housing)
    image.save()
    return render(request, 'normalUser.html')

def registration_view (request):
    data = request.POST.copy()
    username = data.get('username')
    name = data.get('name')
    surname = data.get('surname')
    email= data.get('email')
    password = data.get('password')
    new_user = User.objects.create_user(username=username, email=email, password=password, first_name=name, last_name=surname)
    new_user.save()
    createduser = authenticate(request, username=username, password=password)
    if createduser is not None:
        auth_login(request, createduser)
        return redirect('user')
    else:
        return redirect('signup')


def login_view(request):
    data = request.POST.copy()
    username = data.get('username')
    password = data.get('password')
    loggedinuser = authenticate(request, username=username, password=password)
    if loggedinuser is not None:
        auth_login(request, loggedinuser)
        return redirect('user')
    else:
        return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('index.html')

def forgetPassRedirect(request):
    return render(request, 'forgetPassTemplate.html')

def forgetPass(request):
    data = request.POST.copy()
    username = data.get('username')
    newpassword = data.get('password')
    u = User.objects.get(username=username)
    u.set_password(newpassword)
    u.save()
    return redirect('login')

def changeEmail(request):
    data = request.POST.copy()
    new_email = data.get('newEmail')

    if request.user.is_authenticated:
        request.user.email = new_email
        request.user.save()

    return redirect('user')


# def userHomepage(request):
#     usernameHome = None
#     if request.user.is_authenticated:
#         usernameHome = request.user.username
#     return render(request, 'userHome.html', {'username': usernameHome})


def searchResults(request):
    # return render(request, 'index.html', {'JSON': json})
    if request.method == 'GET':
        locality = request.GET.get('section')
        # print(locality)
        h = Housing.objects.filter(locality=locality)

        # house_serializer = serializers.serialize("json", h)
        # json = JsonResponse(house_serializer, safe=False)
        # return (json)
        usernameHome = None
        if request.user.is_authenticated:
            usernameHome = request.user.username
        gotodiv = "sectionSearch"
        return render(request, 'index.html', {'results': h,'username':usernameHome,'jump':gotodiv})

def showMyHomes(request):
    estate = None
    if request.user.is_authenticated:
        estate = request.user.username
    # print(locality)
    h = Housing.objects.filter(estate=estate)
    usernameHome = None
    if request.user.is_authenticated:
        usernameHome = request.user.username
    gotodiv = 'sec4Grid'
    return render(request, 'normalUser.html', {'results': h, 'username':usernameHome, 'jump':gotodiv})


def addComment(request):
    global id
    data = request.POST.copy()
    comment = data.get('feedback')
    houseID = id
    curr_time = datetime.datetime.now()
    usernameHome = None
    if request.user.is_authenticated:
        usernameHome = request.user.username
    new_comment = Comment(time=curr_time, houseID=houseID, comment=comment)
    new_comment.save()
    h = Comment.objects.filter(houseID=houseID)
    return render(request, 'occasion.html',{'comments': h,'id': id,'username': usernameHome})







def occasionPage(request):
    # id = request.META['QUERY_STRING']
    myid = request.GET['id']
    global id
    id = myid
    # vid = id
    # print(locality)
    h = Comment.objects.filter(houseID=myid)
    usernameHome = None
    if request.user.is_authenticated:
        usernameHome = request.user.username

    return render(request, 'occasion.html', {'comments': h,"username": usernameHome})





















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










