def load(path):
    user_list = []
    with open(path, "r") as users:
        for user in users:
            user = user.replace("\n", "")
            user = user.split(",")
            user[2] = bool(int(user[2]))
            if not user[-1].__eq__(''):
                user.append({'SEX': bool(int(user.pop()))})
            else:
                user.pop()
            user_list.append(user)
    return user_list
