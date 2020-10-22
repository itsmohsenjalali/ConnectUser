from PeopleConnection import Connection
import datetime


def load(path, history, connector):
    with open(path, "r") as histories:
        for raw in histories:
            raw = raw.replace("\n", "")
            date, caller_phone_number, receiver_phone_number = raw.split(",")
            caller = [i for i in connector.user_list if i.phone_number == caller_phone_number][0]
            receiver = [i for i in connector.user_list if i.phone_number == receiver_phone_number][0]
            date = datetime.datetime.strptime(date, '%Y-%m-%d')
            history.connections = Connection.Connection(caller=caller, receiver=receiver, date=date)


def save(path, history):
    with open(path, "a") as histories:
        for connection in history.connections:
            caller = connection.caller.phone_number
            receiver = connection.receiver.phone_number
            date = str(connection.date).split(" ")[0]
            histories.write(f"{date},{caller},{receiver}\n")
