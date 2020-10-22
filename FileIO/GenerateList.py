def save(connection_list: list, path: str):
    with open(path, "w") as file:
        for item in connection_list:
            file.write(f"{item.caller} -> {item.receiver}\n")
