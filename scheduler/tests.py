from django.test import TestCase
from django.contrib.auth.models import User
from .models import ScheduleMeeting


# test schedule meeting model
class ScheduleMeetingModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        self.meeting = ScheduleMeeting.objects.create(
            meetingTitle='Test Meeting',
            meetingDate='2026-05-01',
            meetingTime='10:30',
            meetingPlatform='zoom',
            meetingMessage='Testing schedule meeting',
            scheduleType='weekly',
            createdBy=self.user
        )

    # test meeting is created
    def test_meeting_created(self):
        self.assertEqual(self.meeting.meetingTitle, 'Test Meeting')

    # test string returns meeting title
    def test_meeting_string(self):
        self.assertEqual(str(self.meeting), 'Test Meeting')

    # test meeting belongs to user
    def test_meeting_created_by_user(self):
        self.assertEqual(self.meeting.createdBy.username, 'testuser')

    # test platform value
    def test_meeting_platform(self):
        self.assertEqual(self.meeting.meetingPlatform, 'zoom')

    # test schedule type value
    def test_schedule_type(self):
        self.assertEqual(self.meeting.scheduleType, 'weekly')