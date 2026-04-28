def notifications(request):
    if request.user.is_authenticated:
        unread_notifications = request.user.notification_set.filter(is_read=False)
        return {
            "unread_notifications": unread_notifications,
            "unread_notification_count": unread_notifications.count(),
        }

    return {
        "unread_notifications": [],
        "unread_notification_count": 0,
    }