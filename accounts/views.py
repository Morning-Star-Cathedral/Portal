from django.shortcuts import render, redirect
from .forms import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# @login_required(login_url='login_user')
def register_user(request):
    if request.user.is_authenticated:
        return redirect('ChurchDashboard:home_page')
    else:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('user')
                messages.success(request, 'Accounts was created ' + str(user))
                email = form.cleaned_data['email']
                password = form.cleaned_data['password1']

                return redirect('accounts:login_user')
        else:
            form = CustomUserCreationForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)


# @login_required(login_url='login_user')
def edit_user(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:login_user')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {'form': form}
    return render(request, 'accounts/update.html', context)


# @login_required(login_url='login_user')
def LogoutUser(request):
    logout(request)
    return redirect('accounts:login_user')


@csrf_exempt
# @login_required(login_url='login_user')
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('ChurchDashboard:home_page')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('ChurchDashboard:home_page')
            else:
                messages.info(request, 'Email or Password is not correct')
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return render(request, 'accounts/login.html',{})

        context = {}
        return render(request, 'accounts/login.html', context)
