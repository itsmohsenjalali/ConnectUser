import datetime
from .User import User


class Connection:
    def __init__(self, caller: User, receiver: User, date: datetime):
        self.caller = caller
        self.receiver = receiver
        self.date = date
