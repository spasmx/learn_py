# 7.1
print('Which car are you want to rent?')
car = input('Enter the car: ')
print(f'Let me see if I can find you a {car.title()}')

# 7.2
print('Hi!\nHow many people would you like to book a table for?')
people_count = int(input())
if people_count > 8:
    print('Sorry, but now there is no free table.\nWill have to wait')
else:
    print('Your table is ready')

# 7.3
num = int(input('Enter the num: '))
if num % 10 == 0:
    print('Your num is a multiple 10')
else:
    print('Your num is not a multiple 10')

# 7.4
#pizza's ingredients

user_pizza = []

while True:
    ingredients = input('Please, enter ingredient would you like to add in your pizza:\n')
    if ingredients in user_pizza:
        print(f'Your ingredient is already added to the pizza')
        continue
    if ingredients == 'quit':
        break
    print(f'You add the {ingredients} in your pizza')
    user_pizza.append(ingredients)
    print(user_pizza)

# 7.5
while True:
    age = int(input('Enter you age: '))
    if age < 3:
        print('Ticket - free')
    elif 3 <= age < 12:
        print('Ticket - 10$')
    elif age >= 12:
        print('Ticket - 15$')
    if age == 0:
        print('Ha-ha')
        break

# 7.6
number = 0
while number < 3:
    age = int(input('Enter you age: '))
    if age < 3:
        print('Ticket - free')
    elif 3 <= age < 12:
        print('Ticket - 10$')
    elif age >= 12:
        print('Ticket - 15$')

    quit = input('Enter "quit" if you want exit\nDo you want exit?: ')
    if quit == 'quit':
        break
    number += 1

# 7.7
num = 1
while num < 2:
    print('Dont do it ')

# 7.8
sandwich_orders = ['meat', 'tuna', 'vegan', 'pepperoni', 'butter']
sandwich = 0
finished_sandwich = []

while sandwich < len(sandwich_orders):
    finished_sandwich.append(sandwich_orders[sandwich] + ' sandwich')
    print(f'I made your {sandwich_orders[sandwich]} sandwich')
    sandwich += 1
    if len(sandwich_orders) == len(finished_sandwich):
        print(f"Ive cocked: {', '.join(finished_sandwich).title()}")

# 7.9
sandwich_orders = ['meat', 'pastrami', 'tuna', 'vegan', 'pastrami', 'pepperoni', 'pastrami', 'butter']
sandwich = 0
finished_sandwich = []

print('In our cafe ended pastrami')

# 7.10
question = ['Wats your name?', 'Were you from?', 'What countries your would like a traveling?']
users = []
answers = {}
q = 0

while q < len(question):
    answer = input(f'{question[q]}: ')
    answers[question[q]] = answer
    q += 1

users.append(answers)

for q, a in answers.items():
    print(f'{q} - {a}')


while sandwich < len(sandwich_orders):
    if sandwich_orders[sandwich] == 'pastrami':
        sandwich_orders.remove('pastrami')
    finished_sandwich.append(sandwich_orders[sandwich] + ' sandwich')
    print(f'I made your {sandwich_orders[sandwich]} sandwich')
    sandwich += 1
    if len(sandwich_orders) == len(finished_sandwich):
        print(f"Ive cocked: {', '.join(finished_sandwich).title()}")

# 7.10
