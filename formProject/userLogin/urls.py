from . import views
from django.urls import path



urlpatterns = [

    path('register/',views.register),
    path('login/',views.login),
    # path('registerformsubmit/', views.getregister),
    path('',views.home),
    path('datashow/',views.loginview),
    # path('loginformsubmit/',views.getlogin),
    path('editprofile/',views.editprofile),
    path('lobby/', views.room, name='room'),
]
