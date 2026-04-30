from django.urls import path
from .views import signup, home, user_logout, teams, team_detail, organisation, conversations, chat, start_conversation, hide_conversation, export_excel_report, export_pdf_report, reports_page, export_full_chat_excel, export_full_chat_pdf, LockedLoginView, drafts_page, edit_draft, delete_draft, mark_notifications_read, updateprofile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('accounts/login/', LockedLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='user_logout'),
    path('profile/', updateprofile, name='updateprofile'),
    path('teams/', teams, name='teams'),
    path('teams/<int:team_id>/', team_detail, name='team_detail'),
    path('organisation/', organisation, name='organisation'),
    path('chat/', conversations, name='inbox'),
    path("drafts/", drafts_page, name="drafts_page"),
    path('chat/<int:conversation_id>/', chat, name='chat'),
    path('start/<int:user_id>/', start_conversation, name='start_conversation'),
    path('chat/hide/<int:conversation_id>/', hide_conversation, name='hide_conversation'),
    path("reports/", reports_page, name="reports_page"),
    path("reports/excel/", export_excel_report, name="export_excel_report"),
    path("reports/pdf/", export_pdf_report, name="export_pdf_report"),
    path("reports/full-chat/excel/", export_full_chat_excel, name="export_full_chat_excel"),
    path("reports/full-chat/pdf/", export_full_chat_pdf, name="export_full_chat_pdf"),
    path("drafts/<int:draft_id>/edit/", edit_draft, name="edit_draft"),
    path("drafts/<int:draft_id>/delete/", delete_draft, name="delete_draft"),
    path("notifications/read/", mark_notifications_read, name="mark_notifications_read"),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    ]
