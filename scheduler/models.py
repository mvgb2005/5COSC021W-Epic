from django.db import models
from django.contrib.auth.models import User


# create meeting model
class ScheduleMeeting(models.Model):
    PLATFORM = [
        ('zoom', 'Zoom'),
        ('teams', 'Microsoft Teams'),
        ('google_meet', 'Google Meet'),
    ]

    SCHEDULE_TYPE = [
        ('upcoming', 'Upcoming'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]

    meetingTitle = models.CharField(max_length=100)  # store meeting title
    meetingDate = models.DateField()  # store meeting date
    meetingTime = models.TimeField()  # store meeting time
    meetingPlatform = models.CharField(max_length=30, choices=PLATFORM)  # store platform
    meetingMessage = models.TextField(blank=True)  # store meeting message
    scheduleType = models.CharField(max_length=20, choices=SCHEDULE_TYPE, default='upcoming')  # store type
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)  # store meeting owner
    createdAt = models.DateTimeField(auto_now_add=True)  # store created date
    updatedAt = models.DateTimeField(auto_now=True)  # store updated date

    # show title in admin
    def __str__(self):
        return self.meetingTitle