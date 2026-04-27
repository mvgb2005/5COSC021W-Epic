from django.urls import path
from .views import signup, home, user_logout, teams, team_detail, organisation, conversations, chat, start_conversation, hide_conversation, export_excel_report, export_pdf_report, reports_page, export_full_chat_excel, export_full_chat_pdf, LockedLoginView

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('accounts/login/', LockedLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('teams/', teams, name='teams'),
    path('teams/<int:team_id>/', team_detail, name='team_detail'),
    path('organisation/', organisation, name='organisation'),
    path('chat/', conversations, name='inbox'),
    path('chat/<int:conversation_id>/', chat, name='chat'),
    path('start/<int:user_id>/', start_conversation, name='start_conversation'),
    path('chat/hide/<int:conversation_id>/', hide_conversation, name='hide_conversation'),
    path("reports/", reports_page, name="reports_page"),
    path("reports/excel/", export_excel_report, name="export_excel_report"),
    path("reports/pdf/", export_pdf_report, name="export_pdf_report"),
    path("reports/full-chat/excel/", export_full_chat_excel, name="export_full_chat_excel"),
    path("reports/full-chat/pdf/", export_full_chat_pdf, name="export_full_chat_pdf"),
    
    ]
