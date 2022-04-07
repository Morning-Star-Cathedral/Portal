from .views import *
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('login/', user_login, name='login_user'),
    path('logout/', logout, name='logout'),
    path('signup/', register_user, name='sign_in'),
    path('update/', edit_user, name='update_url'),

]
