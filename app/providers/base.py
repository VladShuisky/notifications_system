import abc


class NotificationProvider(abc.ABC):
    name: str

    @abc.abstractmethod
    async def send(self, *, message: str, email: str | None, phone: str | None, telegram_chat_id: str | None) -> None:
        """Attempt to send a notification.

        Should raise an exception on failure.
        """
        raise NotImplementedError






