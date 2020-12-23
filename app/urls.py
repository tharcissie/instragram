from django.urls import path
from .views import home, signup, profile, user_profile

urlpatterns = [

    path('', home , name ='home'),
    #path('create_post/', create_post , name ='create_post'),
    path('signup/', signup , name='signup'),
    path('profile/<username>/', profile, name='profile'),
    path('user_profile/<username>/', user_profile, name='user_profile'),


]