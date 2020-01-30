from django.urls import path
# from django.contribs
from . import views

urlpatterns = [
    path('home', views.home, name='index'),
    path('', views.home),
    path('login', views.login, name='login'),
    path('signup', views.loginSignup, name='signup'),
    # path('signup.html', views.signup, name='signup'),
    path('index.html', views.home),
    # path('loginSignup/index.html', views.home),
    # path('occasion.html', views.occasion),
    path('userlevel',views.userlevel,name='userlevel'),
    path('user', views.user, name = 'user'),
    path('manager', views.manager, name='manager'),
    path('addHouse', views.addHousing),
    # path(, include("django.contrib.auth.urls"))
    path('register', views.registration_view),
    path('loggingin', views.login_view),
    path('logout', views.logout_view),
    path('forgetPassRedirect', views.forgetPassRedirect),
    path('forgetPass', views.forgetPass),
    path('changeEmail', views.changeEmail),
    # path('userHomepage', views.userHomepage),
    path('search', views.searchResults),
    path('myHomes', views.showMyHomes),
    path('allHomes', views.showAllHomes),
    path('getAllHome', views.getAll),
    path('allUsers', views.showAllUsers),
    path('addComment', views.addComment),
    path(r'^addCommentSingle/(?P<select>[0-9]+)/$', views.addCommentSingle, name= "addCommentSingle"),
    path('occasion.html',views.occasionPage),
    path(r'^deleteUser/(?P<select>[0-9]+)/$', views.deleteUser, name="deleteUser"),
    path(r'^deleteHousing/(?P<select>[0-9]+)/$', views.deleteHousing, name="deleteHousing"),
    path(r'^starHousing/(?P<select>[0-9]+)/$', views.starHousing, name="starHousing"),
    path(r'^bookmarkHousing/(?P<select>[0-9]+)/$', views.bookmarkHousing, name="bookmarkHousing"),
    path(r'^editHousing/(?P<select>[0-9]+)/$', views.editHousing, name="editHousing"),
    path(r'^addManager/(?P<select>[0-9]+)/$', views.addManager, name="addManager"),
    path(r'^showSpecificHouse/(?P<select>[0-9]+)/$', views.showSpecificHouse, name="showSpecificHouse"),
    path('makeedition', views.makeedition, name="makeedition"),

    # path('addManager', views.addManager),

]