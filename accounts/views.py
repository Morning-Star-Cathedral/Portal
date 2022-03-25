from django.shortcuts import render, redirect
from .forms import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


# Create your views here.

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            request.session['pk'] = user.pk
            return redirect('ChurchDashboard:home_page')

        if 'next' in request.POST:
            return redirect(request.POST.get('next'))
        else:
            return render(request, 'accounts/login.html', {})
    return render(request, 'accounts/login.html', {})
