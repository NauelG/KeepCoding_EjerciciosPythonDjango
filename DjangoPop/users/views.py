from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_user_in_django, logout as finish_user_session

# Create your views here.
from users.forms import RegisterForm


def login(request):

    if request.method == 'POST':
        username = request.POST.get('form_username')
        password = request.POST.get('form_password')
        user = authenticate(request, username=username, password=password)
        if user is None: # Si no existe el usuario con ese username o password
            messages.error(request, 'Wrong username or password')
        else:
            login_user_in_django(request, user)
            welcome_url = request.GET.get('next', 'home')
            return redirect(welcome_url)

    return render(request, 'users/login.html')

def logout(request):
    finish_user_session(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = User()
            new_user.first_name = form.cleaned_data.get('first_name')
            new_user.last_name = form.cleaned_data.get('last_name')
            new_user.username = form.cleaned_data.get('username')
            new_user.email = form.cleaned_data.get('email')
            new_user.set_password(form.cleaned_data.get('password'))
            new_user.save()
            messages.success(request, 'User registered successfully!')
            form = RegisterForm()
        # TODO Procesar el formulario
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})