# 10.1/10.2

my_file = 'learning_python.txt'

with open(my_file) as f:
    # file_1 = f.read()
    # print(file_1)
    file_2 = f.readlines()

    for line in f:
        print(line.rstrip())

file_3 = []
for line in file_2:
    file_3.append(line.replace('\n', ''))
print(file_3)

with open(my_file) as f:
    for line in f:
        print(line.replace('Python', 'C').rstrip())


# 10.3

name = input('What is your name?: ')

with open('quest.txt', 'w') as f:
    file = f.write(name)

# 10.4
print('If you want to exit enter - "y"')
while True:
    guest_name = input('What is your name?: ')
    if guest_name == 'y':
        break
    print(f'Hello {guest_name}!')
    with open('guest_book.txt', 'a') as f:
        file_1 = f.write(f'{guest_name}\n')

# 10.5
print('If you want to exit enter - "y"')
while True:
    answer_about_programming = input('Why do you like programming?: ')
    if answer_about_programming == 'y':
        break
    with open('answers_people.txt', 'a') as f:
        answer = f.write(f'{answer_about_programming}\n')



