class Member:
    id_counter = 1  # щоб створити зовсім унікальний id можна використовувати бібліотеку uuid

    def __init__(self, name, surname, age, join_date):
        self.name = name
        self.surname = surname
        self.age = age
        self.__join = join_date
        self.__user_id = self.id_counter
        Member.id_counter += 1
        self._full_name = None

    @property
    def full_name(self):
        self._full_name = f"{self.name} {self.surname}"
        return self._full_name

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_surname(self, surname):
        self.surname = surname

    def get_surname(self):
        return self.surname

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def get_join_date(self):
        return self.__join

    def get_user_id(self):
        return self.__user_id


class Moderator(Member):
    def __init__(self, name, surname, age, join_date, badge=None):
        super(Moderator, self).__init__(name, surname, age, join_date)
        self.badge = badge

    def set_badge(self, badge):
        self.badge = badge

    def get_badge(self):
        return self.badge


class Admin(Moderator):
    def __init__(self, name, surname, age, join_date, badge=None):
        super(Admin, self).__init__(name, surname, age, join_date, badge)
        self.level = 1

    def set_level(self, level):
        self.level = level

    def get_level(self):
        return self.level
