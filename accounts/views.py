from django.shortcuts import render, redirect
from .forms import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages

# # Create your views here.
# def login_request(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request=request, data=request.POST)
#         if form.is_valid():
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')
#             user = authenticate(email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You are now logged in as {email}")
#                 return redirect('/')
#             else:
#                 messages.error(request, "Invalid username or password.")
#         else:
#             messages.error(request, "Invalid username or password.")
#     form = CustomUserCreationForm()
#     return render(request=request, template_name="accounts/login.html", context={"form": form})
#

def logout_user(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('accounts:login_user')


# @login_required(login_url='users:login')
def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(email=email, password=password)
            login(request, user)

            return redirect('ChurchDashboard:home_page')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


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



def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            request.session['pk'] = user.pk
            return redirect('users:verify')

        if 'next' in request.POST:
            return redirect(request.POST.get('next'))
        else:
            return render(request, "login.html", {})
    return render(request, "login.html", {})






def Logout(request):
    """logout logged in user"""
    logout(request)
    return HttpResponseRedirect(reverse_lazy('custom_auth:dashboard'))



def user_login(request):
    if request.method == 'GET':
        context = ''
        return render(request, 'accounts/login.html', {'context': context})

    elif request.method == 'POST':
        username = request.POST.get('email', '')
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page?
            return redirect('/')
        else:
            context = {'error': 'Wrong credintials'}  # to display error?
            return render(request, 'accounts/login.html', {'context': context})
