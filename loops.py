#for loop on list
monday_temp = [9.1,8.4,5.8]

for temp in monday_temp:
    print(round(temp))

for letter in 'HELLO':
    print(letter)

#for loop on dictionary

stu_grades ={'Mike': 100, 'Chris': 389, 'DS': 123}

for grades in stu_grades.keys():
    print(grades)
# Mike
# Chris
# DS

for grades in stu_grades.items():
    print(grades)
# ('Mike', 100)
# ('Chris', 389)
# ('DS', 123)