# 6.1
user = {
    'first_name': 'Bob',
    'last_name': 'Gibson',
    'age': '21',
    'city': 'Paris'
}
print(user['first_name'])
print(user['last_name'])
print(user['age'])
print(user['city'])
print(user)

# 6.2
favorite_number = {
    'Alex': '13',
    'Bob': '7',
    'Bred': '41',
    'John': '11',
    'Sarah': '88',
}

print(f'Alex. Favorite num - {favorite_number["Alex"]}\nBob. Favorite num - {favorite_number["Bob"]}\n'
      f'Bred. Favorite num - {favorite_number["Bred"]}\nJohn. Favorite num - {favorite_number["John"]}\n'
      f'Sarah. Favorite num - {favorite_number["Sarah"]}')

# 6.3
glossary = {
    'if': 'operator',
    'else': 'block',
    '()': 'tuple',
    '[]': 'list',
    'print()': 'function',
}
print(f'if: \n\t{glossary["if"]}\n')
print(f'else: \n\t{glossary["else"]}\n')
print(f'(): \n\t{glossary["()"]}\n')
print(f'[]: \n\t{glossary["[]"]}\n')
print(f'print(): \n\t{glossary["print()"]}')

# 6.4
glossary = {
    'if': 'operator',
    'else': 'block',
    '()': 'tuple',
    '[]': 'list',
    'print()': 'function',
    'int': 'integer',
    'str': 'string',
    'float': 'floating point',
    '{}': 'dictionary',
    '.title()': 'method'
}

for k, v in glossary.items():
    print(f'{k}: \n\t{v}\n')

# 6.5
rivers = {
    'nile': 'egypt',
    'dnipro': 'ukraine',
    'amazonka': 'brasil'
}

for river, country in rivers.items():
    print(f'The {river.title()} runs through in {country.title()}')

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())

# 6.6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',

}

names_list = ['max', 'bill']
for name in favorite_languages.keys():
    names_list.append(name)

for name in names_list:
    if name in favorite_languages:
        print(f'Thank you for answer, {name.title()}')
    else:
        print(f'{name.title()}, please answer the question')

x = list(range(12))
print(sum(x))
print(len(x))

# 6.7
people1 = {
    'first_name': 'Bob',
    'last_name': 'Gibson',
    'age': '21',
    'city': 'Paris'
}

people2 = {
    'first_name': 'John',
    'last_name': 'Smith',
    'age': '14',
    'city': 'New York'
}

people3 = {
    'first_name': 'GG',
    'last_name': 'Allin',
    'age': '54',
    'city': 'Berlin'
}

peoples = [people1, people2, people3]
for people in peoples:
    print(people)

# 6.8
pet1 = {
    'class': 'cat',
    'pet_name': 'garffield',
    'age': '1',
    'owner': 'max'
}

pet2 = {
    'class': 'dog',
    'pet_name': 'maylo',
    'age': '4',
    'owner': 'julia'
}

pets = [pet1, pet2]
for pet in pets:
    print('Pet info:')
    for key, value in pet.items():
        print(f'\t{key} - {value.title()}')

# 6.9
favorite_places = {
    'Max': ['square', 'everest'],
    'Anna': ['bitch', 'sea'],
    'Julia': ['restaurant', 'park', 'central square']
}

for names, places in favorite_places.items():
    print(f"{names}'s the most favorite place is:")
    for place in places:
        print(f'\t{place.title()}')

# 6.10
favorite_number = {
    'Alex': ['13', '1'],
    'Bob': ['7', '22', '12'],
    'Bred': '41',
    'John': ['11'],
    'Sarah': ['14', '88'],
}

for names, numbers in favorite_number.items():
    print(f"{names.title()} favorite numbers is: {', '.join(numbers)}")

# 6.11
cities = {
    'kyiv': {
        'country': 'ukraine',
        'population': '2_952_301',
        'fact': 'Andriivska church dote have a bells'
    },
    'paris': {
        'country': 'france',
        'population': '2_148_327',
        'fact': 'the main bell of the Notre Dame Cathedral is named Emmanuel and weighs over 13 tonnes'
    },
    'vienna': {
        'country': 'austria',
        'population': '1_897_491',
        'fact': 'ranked first in the world for quality life five times'
    },
}

for city, info in cities.items():
    print(f'{city.title()}:')
    country = info['country'].title()
    population = info['population'].title()
    fact = info['fact'].title()
    print(f'\tCountry - {country}\n\tPopulation - {population}\n\tInteresting fact of {city.title()} - {fact}')