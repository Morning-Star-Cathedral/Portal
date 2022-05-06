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


@login_required(login_url='login_user')
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


@login_required(login_url='login_user')
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


@login_required(login_url='login_user')
def LogoutUser(request):
    logout(request)
    return redirect('accounts:login_user')


#
# @csrf_exempt
# # @login_required(login_url='login_user')
# def loginPage(request):
#     if request.user.is_authenticated:
#         return redirect('ChurchDashboard:home_page')
#     else:
#         if request.method == 'POST':
#             email = request.POST.get('email')
#             password = request.POST.get('password')
#
#             user = authenticate(email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('ChurchDashboard:home_page')
#             else:
#                 messages.info(request, 'Email or Password is not correct')
#             if 'next' in request.POST:
#                 return redirect(request.POST.get('next'))
#             else:
#                 return render(request, 'accounts/login.html', {})
#
#         context = {}
#         return render(request, 'accounts/login.html', context)


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
            else:
                message = 'Login failed!'
    return render(
        request, 'authentication/login.html', context={'form': form, 'message': message})


def loginPage(request):
    logout(request)
    email = password = ''

    if request.POST:
        email = request.POST.get['email']
        password = request.POST.get['password']

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('ChurchDashboard:home_page')
    return render(request, 'accounts/login.html')


def login_user(request):

    email = password = ''
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(email=email, password = password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('ChurchDashboard:home_page')
    return render(request, 'accounts/login.html')


def login_view(request,*args,**kwargs):
    context= {}
    user = request.user
    if user.is_authenticated:
        return redirect('ChurchDashboard:home_page')


    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password =request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                destination = get_redirect_if_exists(request)
                if destination:
                    return redirect(destination)
                return redirect('ChurchDashboard:home_page')
        else:
            context['login_form'] = form
    return render(request,'accounts/login.html', context)


def get_redirect_if_exists(request):
    redirect =None
    if request.GET:
        if request.GET.get('next'):
            redirect = str(request.GET.get('next'))
    return redirect