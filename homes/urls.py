from django.urls import path
# from django.contribs
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.loginSignup, name='signup'),
    # path('signup.html', views.signup, name='signup'),
    path('index.html', views.home),
    # path('loginSignup/index.html', views.home),
    path('occasion.html', views.occasion),
    path('user', views.user, name = 'user'),
    path('addHouse', views.addHousing),
    # path(, include("django.contrib.auth.urls"))
    path('register', views.registration_view),




]