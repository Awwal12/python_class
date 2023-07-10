import time as t


class User:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self) -> str:
        return self.name


class Attendance:
    def __init__(self):
        self.groups = []

    def add_group(self, group: Group):
        self.groups.append(group)

    def add_user_to_group(self, group: str, user: User):
        if len(self.groups) != 0:
            for i in self.groups:
                if i == group:
                    i.add_user(user)
                    return f"{user} has been added to {group}"


class Group:
    def __init__(self, name) -> None:
        self.name = name

    def addNames():
        for x in names:
            if x != names:
                names.append(x)
        return names
