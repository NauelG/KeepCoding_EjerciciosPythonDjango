from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_user_in_django

# Create your views here.

def login(request):

    if request.method == 'POST':
        username = request.POST.get('form_username')
        password = request.POST.get('form_password')
        user = authenticate(request, username=username, password=password)
        if user is None: # Si no existe el usuario con ese username o password
            messages.error(request, 'Wrong username or password')
        else:
            login_user_in_django(request, user)
            return redirect('home')

    return render(request, 'users/login.html')