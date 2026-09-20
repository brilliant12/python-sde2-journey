from abc import ABC, abstractmethod


class NotificationService(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass


class ConsoleNotificationService(NotificationService):
    def send(self, message: str) -> None:
        print(f"[Console] {message}")


class EmailNotificationService(NotificationService):
    def send(self, message: str) -> None:
        print(f"[Email] Sending: {message}")