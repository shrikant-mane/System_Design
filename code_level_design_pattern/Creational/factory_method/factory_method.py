from abc import ABC, abstractmethod

# product
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

# Concrete Product
class SMSNotification(Notification):
    def send(self, message):
        print(f"SMS : {message}")

class EmailNotification(Notification):
    def send(self, message):
        print(f"Email : {message}")

class PushNotification(Notification):
    def send(self, message):
        print(f"Push Notice: {message}")


# creator
class NotificationService(ABC):
    @abstractmethod
    def create_notification(self):
        pass

    def notify(self, message):
        notification = self.create_notification()
        notification.send(message)

# concrete creator
class EmailNotificationService(NotificationService):
    def create_notification(self):
        return EmailNotification()

class SMSNotificationService(NotificationService):
    def create_notification(self):
        return SMSNotification()

class PushNotificationService(NotificationService):
    def create_notification(self):
        return PushNotification()


client = EmailNotificationService()
client.notify("Email send ")


"""
| Component        | Example                    |
| ---------------- | -------------------------- |
| Product          | `Notification`             |
| Concrete Product | `EmailNotification`        |
| Concrete Product | `SMSNotification`          |
| Concrete Product | `PushNotification`         |
| Creator          | `NotificationService`      |
| Factory Method   | `create_notification()`    |
| Concrete Creator | `EmailNotificationService` |
| Client           | Application code           |

"""