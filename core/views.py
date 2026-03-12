from urllib import response
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .forms import SignUpForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
@never_cache
def home(request):
    return render(request, 'home.html')

def user_logout(request):
    if request.method == 'POST':
        logout(request)
    return redirect('/accounts/login/')

@login_required
@never_cache
def teams(request):
    return render(request, 'teams.html')

@login_required
@never_cache
def team_detail(request, team_id):
    return render(request, 'team_detail.html', {'team_id': team_id})

@login_required
@never_cache
def organisation(request):
    return render(request, 'organisation.html')


