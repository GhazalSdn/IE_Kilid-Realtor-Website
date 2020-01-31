from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from homes.models import Housing, kilidUser,Comment, Bookmark
from homes.models import Image as modelImage
from django.contrib.auth.models import User
# from homes.forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.core import serializers
from django.contrib import messages
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
# def signup(request):
#     return render(request, 'signup.html')

# def occasion(request):
#     return render(request, 'occasion.html')
def user(request):
    usernameHome = None
    if request.user.is_authenticated:
        usernameHome = request.user.username
    return render(request, 'normalUser.html',{'username': usernameHome})

def manager(request):
    usernameHome = None
    if request.user.is_authenticated:
        usernameHome = request.user.username
    return render(request, 'manager.html',{'username': usernameHome})



def userlevel(request):
    kilidU = kilidUser.objects.filter(user=request.user)[0]
    if (kilidU.isManager == False):
        return redirect('user')
    else:
        return redirect('manager')


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
    curr_time = datetime.datetime.now()
    image = modelImage(image='/static/homeImgs/'+pic)
    image.save()
    estate = None
    if request.user.is_authenticated:
        estate = request.user.username
    housing = Housing(title=title, price=price, type=type, area=area, bedrooms=bedrooms, parkings=parkings, locality=locality, created_at=curr_time, estate=estate, pic=image)
    housing.save()
    messages.error(request, '- خانه اضافه شد.')
    kilidU = kilidUser.objects.filter(user=request.user)[0]
    if (kilidU.isManager == False):
        return redirect('user')
    else:
        return redirect('manager')


def registration_view (request):
    data = request.POST.copy()
    username = data.get('username')
    name = data.get('name')
    surname = data.get('surname')
    email= data.get('email')
    password = data.get('password')
    if User.objects.filter(username=username).exists():
        messages.error(request, '- نام کاربری وارد شده تکراری است')
        return redirect('signup')

    new_user = User.objects.create_user(username=username, email=email, password=password, first_name=name, last_name=surname)
    new_user.save()
    # new_kilidUser = kilidUser(user= new_user, isManager=False)
    # new_kilidUser.save()
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
        kilidU = kilidUser.objects.filter(user=loggedinuser)[0]
        if(kilidU.isManager == False):
            return redirect('user')
        else:
            return redirect('manager')

    else:
        messages.error(request, '- اطلاعات کاربر نادرست است.')
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
    messages.error(request, '- گذرواژه تغییر یافت')
    return redirect('login')

def changeEmail(request):
    data = request.POST.copy()
    new_email = data.get('newEmail')

    if request.user.is_authenticated:
        request.user.email = new_email
        request.user.save()
    messages.error(request, '- ایمیل به روزرسانی شد')
    kilidU = kilidUser.objects.filter(user=request.user)[0]
    if (kilidU.isManager == False):
        return redirect('user')
    else:
        return redirect('manager')

    # return redirect('user')


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
        return render(request, 'index.html', {'results': h,'username':usernameHome, 'jump':gotodiv})



def advancedSearchResults(request):

    minP = 0
    maxP = 900000
    minA =0
    maxA = 900000
    # return render(request, 'index.html', {'JSON': json})
    if request.method == 'GET':
        locality = request.GET.get('section')
        if request.GET['minP']:
            minP = request.GET.get('minP')
        if request.GET['maxP']:
            maxP = request.GET.get('maxP')
        if request.GET['minA']:
            minA = request.GET.get('minA')
        if request.GET['maxA']:
            maxA = request.GET.get('maxA')
        # print(locality)
        h = Housing.objects.filter(locality=locality, price__gte=minP, price__lte=maxP, area__gte=minA, area__lte=maxA)
        # house_serializer = serializers.serialize("json", h)
        # json = JsonResponse(house_serializer, safe=False)
        # return (json)
        usernameHome = None
        if request.user.is_authenticated:
            usernameHome = request.user.username

        gotodiv = "sectionSearch"
        return render(request, 'index.html', {'results': h,'username':usernameHome, 'jump':gotodiv})



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
    return render(request, 'occasion.html', {'comments': h, 'id': houseID,'username': usernameHome})







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


def showAllHomes(request):

    h = Housing.objects.all()
    usernameHome = None
    if request.user.is_authenticated:
        usernameHome = request.user.username
    gotodiv = 'sec4HeadHome'
    return render(request, 'manager.html', {'results': h, 'username': usernameHome, 'jump': gotodiv})



def getAll(request):

    h = Housing.objects.all()
    usernameHome = None
    if request.user.is_authenticated:
        usernameHome = request.user.username
    gotodiv = 'sec4HeadHome'
    return render(request, 'index.html', {'allresults': h, 'username': usernameHome, 'jump': gotodiv})


def showAllUsers(request):
   myusers = kilidUser.objects.all()
   usernameHome = None
   if request.user.is_authenticated:
       usernameHome = request.user.username
   gotodiv = 'sec4HeadUser'
   return render(request, 'manager.html', {'myUsers': myusers, 'username': usernameHome, 'jump': gotodiv})



def deleteUser(request,select):
    # selected = request.GET['select']
    selectU = User.objects.filter(username=select)[0]
    selectU.delete()

    kilidU = kilidUser.objects.filter(user=request.user)[0]
    messages.error(request, '- کاربر حذف شد')
    if (kilidU.isManager == False):
        return redirect('user')
    else:
        return redirect('manager')




def deleteHousing(request, select):
    selectU = Housing.objects.filter(id=select)[0]
    selectU.delete()

    kilidU = kilidUser.objects.filter(user=request.user)[0]
    messages.error(request, '- خانه حذف شد')
    if (kilidU.isManager == False):
        return redirect('user')
    else:
        return redirect('manager')



def addManager(request, select):
    selectU = User.objects.filter(username=select)[0]
    kilidU = kilidUser.objects.filter(user=selectU)[0]
    kilidU.isManager = True
    kilidU.save()

    kilidU = kilidUser.objects.filter(user=request.user)[0]
    messages.error(request, '- ارتقا کاربر انتخاب شده به مدیر')
    if (kilidU.isManager == False):
        return redirect('user')
    else:
        return redirect('manager')

def starHousing(request,select):
    selectU = Housing.objects.filter(id=select)[0]
    selectU.star = True
    selectU.save()
    kilidU = kilidUser.objects.filter(user=request.user)[0]
    messages.error(request, '- خانه به اکازیون اضافه شد')
    if (kilidU.isManager == False):
        return redirect('user')
    else:
        return redirect('manager')

def bookmarkHousing(request, select):
        selectU = Housing.objects.filter(id=select)[0]
        # selectU.bookmark = True
        # selectU.save()
        kilidU = kilidUser.objects.filter(user=request.user)[0]
        new_bookmark = Bookmark(user=kilidU, house=selectU)
        new_bookmark.save()
        messages.error(request, '- خانه به bookmark اضافه شد')
        if (kilidU.isManager == False):
            return redirect('user')
        else:
            return redirect('manager')


def editHousing(request,select):
    selectU = Housing.objects.filter(id=select)[0]
    gotodiv = 'editionDiv'
    usernameHome = None
    if request.user.is_authenticated:
        usernameHome = request.user.username
    kilidU = kilidUser.objects.filter(user=request.user)[0]

    if (kilidU.isManager == False):

        return render(request, 'normalUser.html', {'houseID': selectU.id,'title':selectU.title,'price':selectU.price,'type':selectU.type,'area':selectU.area,'bedrooms':selectU.bedrooms,
                      'parkings':selectU.parkings,'locality':selectU.locality, 'username': usernameHome, 'jump': gotodiv, 'edition':True})
    else:
        return render(request, 'manager.html', {'houseID': selectU.id,'title':selectU.title,'price':selectU.price,'type':selectU.type,'area':selectU.area,'bedrooms':selectU.bedrooms,
                      'parkings':selectU.parkings,'locality':selectU.locality,'username': usernameHome, 'jump': gotodiv, 'edition':True})




def bookmarks(request):
    usernameHome = None
    if request.user.is_authenticated:
        usernameHome = request.user.username
    kilidU = kilidUser.objects.filter(user=request.user)[0]
    bookmarks = Bookmark.objects.filter(user=kilidU)
    gotodiv = 'sec4Head‌Bookmark'

    if (kilidU.isManager == False):

        return render(request, 'normalUser.html', {'bookmarks':bookmarks,'username': usernameHome, 'jump': gotodiv})
    else:
        return render(request, 'manager.html', {'bookmarks':bookmarks,'username': usernameHome, 'jump': gotodiv})




def makeedition(request):
    select = request.POST['select']
    selectU = Housing.objects.filter(id=select)[0]
    if request.POST['hometitle']:
        selectU.title = request.POST['hometitle']
    if request.POST['homeprice']:
        selectU.price = request.POST['homeprice']
    if request.POST['hometype']:
        selectU.type = request.POST['hometype']
    if request.POST['homearea']:
        selectU.area = request.POST['homearea']
    if request.POST['homebedrooms']:
        selectU.bedrooms = request.POST['homebedrooms']
    if request.POST['homeparkings']:
        selectU.parkings = request.POST['homeparkings']
    if request.POST['homelocality']:
        selectU.locality = request.POST['homelocality']
    selectU.save()
    messages.error(request, '- خانه ویرایش شد')

    kilidU = kilidUser.objects.filter(user=request.user)[0]
    if (kilidU.isManager == False):
        return redirect('user')
    else:
        return redirect('manager')



def showSpecificHouse(request, select):
    selectU = Housing.objects.filter(id=select)[0]
    h = Comment.objects.filter(houseID=selectU.id)
    usernameHome = None
    if request.user.is_authenticated:
        usernameHome = request.user.username
    return render(request, 'singleHome.html', {'comments': h, 'result':selectU, 'username': usernameHome})

def addCommentSingle(request,select):
    selectU = Housing.objects.filter(id=select)[0]

    data = request.POST.copy()
    comment = data.get('feedback')
    houseID = selectU.id
    curr_time = datetime.datetime.now()
    usernameHome = None
    if request.user.is_authenticated:
        usernameHome = request.user.username
    new_comment = Comment(time=curr_time, houseID=houseID, comment=comment)
    new_comment.save()
    h = Comment.objects.filter(houseID=houseID)
    return render(request, 'singleHome.html', {'comments': h, 'result': selectU, 'username': usernameHome})





































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










