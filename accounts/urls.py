from .views import *
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('login/', login_user, name='login_user'),
    path('logout/', logout, name='logout'),
    path('signin/', register_user, name='sign_in'),
    path('update/', edit_user, name='update_url'),
]
