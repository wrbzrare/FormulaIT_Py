# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator=','):
    split_group1 = set(group1.split(separator))
    split_group2 = set(group2.split(separator))
    return sorted(split_group1 & split_group2)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
participants = find_common_participants(participants_first_group, participants_second_group, '|')
print(participants)
