class User:
    def __init__(self, phone_number: str, name: str, sex: bool, block: dict = {}):
        self.name = name
        self.phone_number = phone_number
        self.sex = sex
        self.block = block

    def __str__(self):
        return f"{self.name}"
