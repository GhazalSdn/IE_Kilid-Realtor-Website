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
    path('user', views.user, name = 'user'),
    path('manager', views.manager),
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
    path('addComment', views.addComment),
    path('occasion.html',views.occasionPage),




]