from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
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
def conversations(request):
    delete_empty_conversations()
    conversations = Conversation.objects.filter(participants=request.user, messages__isnull=False).exclude(hidden_for=request.user).distinct().order_by('-lastUpdated')
    users = User.objects.exclude(id=request.user.id).order_by('username')
    hidden_for = models.ManyToManyField(User, related_name='hidden_conversations', blank=True)
    return render(request, 'messaging/conversations.html', {'conversations': conversations, 'users': users})

@login_required
def start_conversation(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    convos = Conversation.objects.filter(participants=request.user).filter(participants=other_user)
    convo = convos.first()
    # solves duplication glitch
    if convos.count() > 1:
        convos.exclude(id=convo.id).delete()
    if convo:
        convo.hidden_for.remove(request.user)
    else:
        convo = Conversation.objects.create()
        convo.participants.add(request.user, other_user)
    return redirect('chat', conversation_id=convo.id)

@login_required
def chat(request, conversation_id):
    convo = Conversation.objects.filter(id=conversation_id).first()
    if not convo:
        return redirect('conversations')
    if request.user not in convo.participants.all():
        return redirect('conversations')
    messages = Message.objects.filter(conversation=convo).order_by('timestamp')
    users = User.objects.exclude(id=request.user.id).order_by('username')
    conversations = Conversation.objects.filter(participants=request.user).exclude(hidden_for=request.user).distinct().order_by('-lastUpdated')
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(conversation=convo, sender=request.user, content=content)
        return redirect('chat', conversation_id=convo.id)
    return render(request, 'messaging/chat.html', {'conversation': convo,'messages': messages,'users': users,'conversations': conversations})

def delete_empty_conversations():
    empty_convos = Conversation.objects.filter(messages__isnull=True)
    empty_convos.delete()

@login_required
def hide_conversation(request, conversation_id):
    convo = get_object_or_404(Conversation, id=conversation_id)
    convo.hidden_for.add(request.user)
    return redirect('inbox')