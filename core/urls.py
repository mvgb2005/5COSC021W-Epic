from django.urls import path
from .views import signup, home, user_logout, teams, team_detail, organisation

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('logout/', user_logout, name='logout'),
    path('teams/', teams, name='teams'),
    path('teams/<int:team_id>/', team_detail, name='teamdetail'),
    path('organisation/', organisation, name='organisation'),
]