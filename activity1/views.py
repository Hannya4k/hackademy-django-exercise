from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegistrationForm
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request, 'activity1/profile.html', context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            profile = Profile.objects.create(user=user)
            profile.save()
            messages.success(
                request, f'Your account has been created! You are now logged in.')
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'activity1/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(
                    request, f'You are now logged in as {username}')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'activity1/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('login')



