from django.urls import path
from .views import signup, home, user_logout, teams, team_detail, organisation, conversations, chat, start_conversation, hide_conversation

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('logout/', user_logout, name='logout'),
    path('teams/', teams, name='teams'),
    path('teams/<int:team_id>/', team_detail, name='team_detail'),
    path('organisation/', organisation, name='organisation'),
    path('chat/', conversations, name='inbox'),
    path('chat/<int:conversation_id>/', chat, name='chat'),
    path('start/<int:user_id>/', start_conversation, name='start_conversation'),
    path('chat/hide/<int:conversation_id>/', hide_conversation, name='hide_conversation'),
    ]
