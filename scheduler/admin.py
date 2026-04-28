from django.contrib import admin
from .models import ScheduleMeeting


# show schedule meetings in admin
class ScheduleMeetingAdmin(admin.ModelAdmin):
    list_display = (
        'meetingTitle',
        'meetingDate',
        'meetingTime',
        'meetingPlatform',
        'scheduleType',
        'createdBy',
    )

    # admin filters
    list_filter = (
        'meetingDate',
        'createdBy',
        'meetingPlatform',
        'scheduleType',
    )

    # admin search
    search_fields = (
        'meetingTitle',
        'meetingMessage',
        'createdBy__username',
    )


# register schedule model in admin panel
admin.site.register(ScheduleMeeting, ScheduleMeetingAdmin)