class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_name(self, name):
        self.__name = name

    def set_access_level(self, access_level):
        if access_level in ['user', 'admin']:
            self.__access_level = access_level
        else:
            raise ValueError("Недостаточно прав")


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'

    def add_user(self, user_list, user):
        if not isinstance(user, User):
            raise TypeError("Пользователь должен быть экземпляром класса User")
        user_list.append(user)
        print(f"Пользователь {user.get_name()} добавлен")

    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                print(f"Пользователь с ID {user_id} именем {user.get_name()} ID {user_id} удален.")
                return
        print(f"Пользователь с таким ID {user_id}. не найден.")


user1 = User(1, "Кирилл")
user2 = User(2, "Ольга")

admin = Admin(0, "Admin")

users = []
admin.add_user(users, user1)
admin.add_user(users, user2)

print(f"Всего пользователей: {len(users)}")

admin.remove_user(users, 1)
print(f"Всего пользователей: {len(users)}")
