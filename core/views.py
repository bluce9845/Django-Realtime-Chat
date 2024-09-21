from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm

def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # authenticated
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('frontpage')
        else:
            return redirect('login')
    else:
        return render(request, 'core/login.html', {})

def logout_view(request):
    logout(request)
    return redirect('frontpage')