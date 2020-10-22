from .User import User
from .History import History
from .Connection import Connection
import random
import datetime


class Connector:
    def __init__(self, user_list):
        self.user_list = []
        for item in user_list:
            self.user_list.append(User(*item))
        admin = User(name="ادمین", phone_number="0000000", sex=True)
        self.user_list.append(admin)
        self.user_not_connect = [i for i in self.user_list]
        if len(user_list) % 2 == 0:
            self.user_not_connect.remove(admin)

    def choice_random(self, history: History, user: User) -> tuple:
        if len(user.block.keys()) > 0:
            white_list = list(filter(lambda partner: block_check(
                caller=user, receiver=partner), self.user_not_connect))
        else:
            white_list = list(filter(lambda partner: history.is_valid(
                caller=user, receiver=partner
            ), self.user_not_connect))
        while True:
            receiver = random.sample(white_list, k=1)[0]
            if user is receiver:
                continue
            flag, index = history.is_exist(caller=user, receiver=receiver)
            if flag:
                if history.is_valid(caller=user, receiver=receiver):
                    return user, receiver, index
            else:
                return user, receiver, index

    def connector(self, history: History):
        connection_list = []
        insensitive = [i for i in self.user_not_connect if len(i.block.keys()) > 0]
        for user in insensitive:
            if user in self.user_not_connect:
                connection = self.create_connection(user=user, history=history)
                history.connections = connection
                connection_list.append(connection)
        for user in self.user_list:
            if user in self.user_not_connect:
                connection = self.create_connection(user=user, history=history)
                history.connections = connection
                connection_list.append(connection)
        return connection_list

    def create_connection(self, user, history):
        caller, receiver, index = self.choice_random(history=history, user=user)
        if index >= 0:
            self.user_not_connect.remove(caller)
            self.user_not_connect.remove(receiver)
            return Connection(caller=history.connections[index].receiver,
                              receiver=history.connections[index].caller,
                              date=datetime.datetime.now())
        else:

            try:
                self.user_not_connect.remove(caller)
                self.user_not_connect.remove(receiver)
            except:
                print("state create_connection")
                print(caller.name, "---", receiver.name)
            return Connection(caller=caller, receiver=receiver, date=datetime.datetime.now())


def block_check(caller, receiver):
    if 'SEX' in caller.block.keys():
        if caller.block['SEX'] == receiver.sex:
            return False
    if 'SEX' in receiver.block.keys():
        if receiver.block['SEX'] == caller.sex:
            return False
    return True
