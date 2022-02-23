# створити пустый список users_list = []
#
# стврорити меню в якому потрібно реалізувати:
#
# 1) додававання нового юзера
# 2) вивід всіх юзерів
# 3) вивід всіх юзерів за віком
# 4) видалення юзера по id
# 5) заміна статуса юзера на протилежний
# 6) вихід з меню
#
# приклад юзера {'id':1,'name':'Max', 'age':35,'status':False}

users_list = []


def users(self, id, name, age, status):
    self.id = id
    self.name = name
    self.age = age
    self.status = status


user1 = {1, 'Max', 35, False}
user2 = {2, 'Diana', 30, True}

users_list.append(user1)
users_list.append(user2)
print(users_list)

# def userAge_key():
#     return users.age
# sort1 = sorted(users_list.age)
# print(sort1)

