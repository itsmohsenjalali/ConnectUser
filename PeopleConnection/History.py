from .Connection import Connection
import datetime


class History:
    def __init__(self):
        self.__connections = []

    def is_exist(self, caller, receiver):
        for index, connection in enumerate(self.__connections):
            if (connection.caller == caller and connection.receiver == receiver) or (
                    connection.caller == receiver and connection.receiver == caller):
                return True, index
        return False, -1

    def is_valid(self, caller, receiver, date: datetime = datetime.datetime.now(), duration: int = 4) -> bool:
        flag, index = self.is_exist(caller, receiver)
        if flag:
            if (self.__connections[index].date - date).days > duration:
                return True
            else:
                return False
        return True

    @property
    def connections(self) -> list:
        return self.__connections

    @connections.setter
    def connections(self, connection: Connection):
        self.__connections.insert(0, connection)
