from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model, logout, update_session_auth_hash



# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def apps(request):
    return render(request, 'apps.html', {})



