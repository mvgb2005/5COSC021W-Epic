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




# Messaging 
@login_required
# inbox view
def conversations(request):
    conversations = Conversation.objects.filter(participants=request.user).order_by('-lastUpdated')
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'messaging/conversations.html', {'conversations': conversations, 'users': users})

# start convo
@login_required
def start_conversation(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    conversation = Conversation.objects.filter(participants=request.user).filter(participants=other_user).first()
    # if not create one
    if not conversation:
        conversation = Conversation.objects.create()
        conversation.participants.add(request.user, other_user)
    return redirect('chat', conversation.id)

# chat view
@login_required
def chat(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id)
    # security check
    if request.user not in conversation.participants.all():
        return redirect('conversations')
    messages = conversation.messages.order_by('timestamp')
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(conversation=conversation, sender=request.user, content=content)
        return redirect('chat', conversation_id)
    return render(request, 'messaging/chat.html', {'conversation': conversation, 'messages': messages})