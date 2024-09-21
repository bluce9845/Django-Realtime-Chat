from django.shortcuts import render
from .forms import SignUpForm

def frontpage(request):
    return render(request, 'core/frontpage.html')