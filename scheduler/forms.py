from django import forms
from .models import ScheduleMeeting


# django meeting form
class ScheduleMeetingForm(forms.ModelForm):
    class Meta:
        model = ScheduleMeeting

        # fields shown in form
        fields = [
            'meetingTitle',
            'meetingDate',
            'meetingTime',
            'meetingPlatform',
            'meetingMessage',
            'scheduleType',
        ]

        
        widgets = {
            'meetingDate': forms.DateInput(attrs={'type': 'date'}),
            'meetingTime': forms.TimeInput(attrs={'type': 'time'}),
            'meetingMessage': forms.Textarea(attrs={'rows': 4}),
        }