

from userAccount import views
from django.urls import path,include

urlpatterns = [
 
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('logout/',views.logout,name='logout'),
     path('forget_password/',views.forget_password,name='forget_password'),
]
