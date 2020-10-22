from FileIO import LoadUser, SaveLoadHistory, GenerateList
from PeopleConnection import GenerateConnection, History


def main():
    history = History.History()
    connections = GenerateConnection.Connector(LoadUser.load("./7am.txt"))
    SaveLoadHistory.load(path='./History_7am.txt', history=history, connector=connections)
    connection_list = connections.connector(history=history)
    GenerateList.save(connection_list=connection_list, path="./list_7am.txt")
    SaveLoadHistory.save(path="./History_7am.txt", history=history)
    history = History.History()
    connections = GenerateConnection.Connector(LoadUser.load("./5am.txt"))
    SaveLoadHistory.load(path='./History_5am.txt', history=history, connector=connections)
    connection_list = connections.connector(history=history)
    GenerateList.save(connection_list=connection_list, path="./list_5am.txt")
    SaveLoadHistory.save(path="./History_5am.txt", history=history)


if __name__ == '__main__':
    main()
