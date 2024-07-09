#Part 2
my_dict = {'Имя':'Геральт', 'Место рождения': 'Ривия', 'Год рождения': 1167}
print('Dict:', my_dict)
print("Existing value:",my_dict['Место рождения'])
print('Not existing value:', my_dict.get('Год смерти'))
my_dict.update({'Прозвище':'Мясник из Блавикена', 'Возраст': 102})
delete_key = my_dict.pop('Место рождения')
print('Deleted value:', delete_key)
print('Updated dict:', my_dict)
#Part 3
my_set = {1, 2, 3, 5, 3, (1, 2, 2, 1, 5), 3, True, 'Witcher', 4.666, 999}
print('Set:', my_set)
my_set.add(7)
my_set.add(52)
my_set.discard(999)
print('Updated set:', my_set)