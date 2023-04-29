# 4.3
for num in range(1, 21):
    print(num)

# 4.4
numbers = list(range(1, 1_000_000 + 1))
for num in numbers:
    print(num)

# 4.5
numbers = list(range(1, 1_000_000 + 1))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4.6
odd_numbers = list(range(1, 20 + 1, 2))
for num in odd_numbers:
    print(num)

# 4.7
numbers_multiples_of_3 = [num for num in range(1, 31) if num % 3 == 0]
for num in numbers_multiples_of_3:
    print(num)

# 4.8
cube_numbers = [num**3 for num in range(1, 11)]
for num in cube_numbers:
    print(num)

# 4.9
cube_numbers1 = [num**3 for num in range(1, 11)]

# 4.10
cube_numbers2 = [num**3 for num in range(1, 10)]
print(cube_numbers)
print(f'The first three item in the list are: {cube_numbers[:3]}')
print(f'Three items from the meddle in the list are: {cube_numbers[3:6]}')
print(f'The last three item in the list are: {cube_numbers[-3:]}')

# 4.11
favorite_pizza = ['pepperoni', 'hawaii', 'margarita', 'four cheese']
friend_pizzas = favorite_pizza[:]

favorite_pizza.append('carbonara')
friend_pizzas.append('beef')

for pizza in favorite_pizza:
    print(f'My favorite pizza are: {pizza}')

for pizza in friend_pizzas:
    print(f"My friend's favorite pizza are: {pizza}")

# 4.12
favorite_pizza = ['pepperoni', 'hawaii', 'margarita', 'four cheese']
friend_pizzas = favorite_pizza[:]

favorite_pizza.append('carbonara')
friend_pizzas.append('beef')

for pizza in favorite_pizza:
    print(f'My favorite pizza are: {pizza}')

for pizza in friend_pizzas:
    print(f"My friend's favorite pizza are: {pizza}")

# 4.13
buffet = ('burger', 'fri', 'cola', 'cesar', 'hot-dog')
print('Menu in buffet')
for dish in buffet:
    print(dish)

buffet = ('burger', 'fri', 'pepsi', 'cesar', 'pizza')
print('New menu in buffet')
for dish in buffet:
    print(dish)


