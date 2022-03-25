from .views import *
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('login/', login_user, name='login_user')
]
