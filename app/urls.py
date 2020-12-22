from django.urls import path
from .views import home, create_post

urlpatterns = [

    path('', home , name ='home'),
    path('create_post/', create_post , name ='create_post'),


]