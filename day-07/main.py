from notification import (
    ConsoleNotificationService,
    EmailNotificationService,
)


def notify_user(notification_service, message):
    notification_service.send(message)


console_service = ConsoleNotificationService()
email_service = EmailNotificationService()

notify_user(console_service, "Day 7 inheritance practice completed.")
notify_user(email_service, "Your Python learning progress was updated.")