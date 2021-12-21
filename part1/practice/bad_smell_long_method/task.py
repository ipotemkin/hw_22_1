csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def _read_users(s: str):
    return [item.split(';') for item in s.split('\n')]


def _sort_users(users_lst: list):
    return sorted(users_lst, key=lambda x: int(x[1]))


def _filter_users(users_lst: list):
    return [user for user in users_lst if int(user[1]) >= 10]


def get_users_list_new(s: str):
    _users = _read_users(s)
    _sorted_users = _sort_users(_users)
    return _filter_users(sorted_users)


# def get_users_list():
#     # Чтение данных из строки
#     data = []
#     for line in csv.split('\n'):
#         name, age = line.split(';')
#         data.append({'name': name, 'age': int(age)})
#
#     # Сортировка по возрасту по возрастанию
#     _new_data = []
#     used_person = set()
#     minimum_age_person = None
#     while len(used_person) != len(data):
#         if minimum_age_person is None:
#             for person in data:
#                 if minimum_age_person is None:
#                     minimum_age_person = person
#                 else:
#                     if person['name'] in used_person:
#                         continue
#                     else:
#                         if person['age'] < minimum_age_person['age']:
#                             minimum_age_person = person
#             _new_data.append(minimum_age_person)
#             used_person.add(minimum_age_person['name'])
#         local_minimum = None
#         for person in data:
#             if person['name'] in used_person:
#                 continue
#             else:
#                 if not local_minimum is None:
#                     if person['age'] < local_minimum['age']:
#                         local_minimum = person
#                 else:
#                     local_minimum = person
#         _new_data.append(local_minimum)
#         used_person.add(local_minimum['name'])
#
#     # Фильтрация
#     result_data = []
#     for person in _new_data:
#         if person['age'] < 10:
#             continue
#         else:
#             result_data.append(person)
#     return result_data


if __name__ == '__main__':
    users = _read_users(csv)
    print(users)
    sorted_users = _sort_users(users)
    print(sorted_users)
    filtered_users = _filter_users(sorted_users)
    print(filtered_users)

    print(get_users_list_new(csv))
