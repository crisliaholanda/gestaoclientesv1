from django.shortcuts import render, redirect
from django.contrib.auth import logout


def home(request):
    return render(request,'home.html')

def logout_page(request):
    logout(request)
    return redirect('home')

