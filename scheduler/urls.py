
from django.urls import path
from . import views

urlpatterns = [

    # show schedule page
    path('', views.schedule_page, name='schedule'),

    # add meeting
    path('create/', views.create_schedule, name='create_schedule'),

    # update meeting
    path('update/<int:schedule_id>/', views.update_schedule, name='update_schedule'),

    # delete meeting
    path('delete/<int:schedule_id>/', views.delete_schedule, name='delete_schedule'),

    # admin reports page
    path('reports/', views.schedule_reports, name='schedule_reports'),

    # export excel report
    path('reports/excel/', views.export_schedule_excel, name='export_schedule_excel'),

    # export pdf report
    path('reports/pdf/', views.export_schedule_pdf, name='export_schedule_pdf'),
]

