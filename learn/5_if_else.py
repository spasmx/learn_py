# 5.1
#write 10 tests who was predict bool value (5 - True, 5 -False )


age = 18
print("age == 18? It's True")
print(age == 18)
print("age == 21? It's False")
print(age == 21)

lang = 'Python'
print("lang == 'Python'? It's True")
print(lang == 'Python')
print("lang == 'C#'? It's False")
print(lang == 'C#')

name = 'Bob'
print("name == 'Bob'? It's True")
print(name == 'Bob')
print("name == 'Bred'? It's False")
print(name == 'Bred')

year = 2022
print("year == 2022? It's True")
print(year == 2022)
print("year == 1995? It's False")
print(year == 1995)

food = 'Pizza'
print("food == 'Pizza'? It's True")
print(food == 'Pizza')
print("food = 'Hot-dog'? It's False")
print(food == 'Hot-dog')

# 5.1
#type cheking(str)
#cheking with .lower() method
#cheking with operators > < >= <=
#cheking with and / or
#checking if an element is in a list
#checking if an element is missing from the list

num = '18'
print(num == '18')
print(num == 18)

mountain = 'Hoverla'
print(mountain.lower() == 'hoverla')
print(mountain.lower() == 'everest')

age = 18
print(0 <= age <= 18)
print(18 < age < 23)

name_1 = 'Bob'
print(name_1 == 'Bob' and 0 <= age <= 18)
print(name_1 == 'Bob' and age == 19)


print(name_1 == 'Mike' or 0 <= age <= 18)
print(name_1 == 'Mike' or age == 19)

fruits = ['banana', 'apple', 'orange']
print('apple' in fruits)
print('avocado' in fruits)

# 5.3
alien_color = 'red'

if alien_color == 'red':
    print('Congratulation! You got 5 points')

if alien_color == 'green':
    pass

# 5.4
alien_color = 'green'
if alien_color == 'green':
    print('Congratulation! You got 5 points')
else:
    print('Congratulation! You got 10 points')


alien_color = 'white'
if alien_color == 'green':
    print('Congratulation! You got 5 points')
else:
    print('Congratulation! You got 10 points')

# 5.5
alien_color = 'green'
if alien_color == 'green':
    print('Congratulation! You got 5 points')
elif alien_color == 'yellow':
    print('Congratulation! You got 10 points')
elif alien_color == 'red':
    print('Congratulation! You got 15 points')

alien_color = 'yellow'
if alien_color == 'green':
    print('Congratulation! You got 5 points')
elif alien_color == 'yellow':
    print('Congratulation! You got 10 points')
elif alien_color == 'red':
    print('Congratulation! You got 15 points')

alien_color = 'red'
if alien_color == 'green':
    print('Congratulation! You got 5 points')
elif alien_color == 'yellow':
    print('Congratulation! You got 10 points')
elif alien_color == 'red':
    print('Congratulation! You got 15 points')

# 5.6
age = int(input("Enter your'e age: "))

if 0 < age < 2:
    print('mini baby'.title())
elif 2 <= age <= 4:
    print('baby'.title())
elif 4 < age < 13:
    print('child'.title())
elif 13 <= age < 20:
    print('teenager'.title())
elif 20 <= age < 65:
    print('adult'.title())
else:
    print('old'.title())

# 5.7
favorite_fruits = ['banana', 'apple', 'mango']

if 'banana' in favorite_fruits:
    print('You really like bananas')
if 'avocado' in favorite_fruits:
    print('You really like avocado')
if 'apple' in favorite_fruits:
    print('You really like apples')
if 'papaya' in favorite_fruits:
    print('You really like papaya')
if 'mango' in favorite_fruits:
    print('You really like mango')

# 5.8
users_name = ['Alex', 'Max', 'admin', 'Kris', 'Sara', ' Bob']

for name in users_name:
    if name == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {name.title()}, thank you for loggin in again')

# 5.9
users_name = []

if users_name:
    for name in users_name:
        if name == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {name.title()}, thank you for loggin in again')
else:
    print('We need to find some users!')

# 5.10
current_users = ['Hum', 'oLoLo', 'Jack', 'Simba', 'Pirat']
current_users_lower = [i.lower() for i in current_users]
new_users = ['Ololo', "OlOlO", 'jacK', 'mr.damage', 'dogstyle', 'ggwp', 'Dino']
print(current_users_lower)
for name in new_users:
    if name.lower() in current_users_lower:
        print('Sorry, this name is already registered')
    else:
        print(f'You have successfully registered with name {name}')

# 5.11
numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}')
