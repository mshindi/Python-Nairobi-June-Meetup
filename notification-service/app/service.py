from app import views
from nameko.events import event_handler


class NotificationService:
    name = "notification_service"

    @event_handler("http_auth_service", "user_created")
    def send_registration_notification(payload):
        views.push_notification(payload)
