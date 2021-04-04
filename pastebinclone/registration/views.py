from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['confirm_password']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('/registration/signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already registered')
                return redirect('/registration/signup')
            else:
                user = User.objects.create_user(username=username, password=pass1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('/registration/login')
        else:
            messages.info(request, 'Passwords do not match...')
            return redirect('/registration/signup')
        return redirect('/pastebin/')
    else:    
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/pastebin/")
        else:
            messages.info(request, 'Invalid username/password')
            return redirect("/registration/login")
    else:
        return render(request, 'login.html')   


def logout(request):
    auth.logout(request)
    return redirect('/pastebin/')

