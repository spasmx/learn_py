import json

# 10.11/10.12


def get_new_favorite_number():
    """Set data from json"""
    file = 'favorite_number.json'
    number = input('What is your favorite number: ')
    with open(file, 'w') as f:
        json.dump(number, f)
    return number


def get_favorite_number():
    """Get data from json"""
    file = 'favorite_number.json'
    try:
        with open(file) as f:
            fav_number = json.load(f)
    except FileNotFoundError:
        return None
    return fav_number


def say_favorite_number():
    """Read data from json"""
    fav_num = get_favorite_number()
    if fav_num:
        print(f'I know your favorite number! It\'s: {fav_num}')
    else:
        fav_num = get_new_favorite_number()
        print(f'I know your favorite number! It\'s: {fav_num}')


say_favorite_number()


# 10.13
def get_stored_username():
    file = 'user_name.json'
    try:
        with open(file) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username(username):
    file = 'user_name.json'
    with open(file, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    username = check_name()
    if username:
        print(f'Welcome back {username}!')


def check_name():
    confirmed_name = input('Confirm your name: ')
    name = get_stored_username()
    if confirmed_name == name:
        return confirmed_name
    else:
        print(f'User {confirmed_name} not found :(')
        username = get_new_username(confirmed_name)
        print(f"We'll remember you when you come back, {username}")


greet_user()

