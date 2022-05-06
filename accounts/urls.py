from .views import *
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('login/', loginPage, name='login_user'),
    path('logout/', LogoutUser, name='logout'),
    path('newdance/', register_user, name='sign_in'),
    path('update/', edit_user, name='update_url'),

]
