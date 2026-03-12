from django.urls import path
from .views import signup, home, user_logout

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('logout/', user_logout, name='logout'),
]