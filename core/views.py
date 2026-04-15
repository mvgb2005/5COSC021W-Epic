from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .forms import SignUpForm
from .models import *

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
    all_teams = Team.objects.select_related('department', 'teamLeader').all()
    return render(request, 'teams.html', {'teams': all_teams})

@login_required
@never_cache
def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)

    members = Membership.objects.filter(team=team)
    repos = Repository.objects.filter(team=team)
    contacts = ContactChannel.objects.filter(team=team)
    updep = Dependency.objects.filter(upstreamDep=team)
    downdep = Dependency.objects.filter(downstreamDep=team)
    return render(request, 'team_detail.html', {
        'team': team,
        'members': members,
        'repositories': repos,
        'contacts': contacts,
        'upstream_dependencies': updep,
        'downstream_dependencies': downdep
    })


@login_required
@never_cache
def organisation(request):
    departments = Department.objects.prefetch_related('team_set').all()
    return render(request, 'organisation.html', {'departments': departments})