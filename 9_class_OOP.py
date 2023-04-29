# 9.1/9.2/9.4
class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self) -> None:
        print(f'Restaurant {self.restaurant_name}, {self.cuisine_type} cuisine')

    def open_restaurant(self) -> None:
        print(f'Restaurant {self.restaurant_name} is open!')

    def set_number_served(self, served_count: int) -> None:
        self.number_served = served_count

    def increment_number_served(self, served_count: int) -> None:
        self.number_served += served_count


rest_amigo = Restaurant('Amigo', 'mexican')


# print(rest_amigo.restaurant_name)
# print(rest_amigo.cuisine_type)
# rest_amigo.describe_restaurant()
# rest_amigo.open_restaurant()

# rest_burger_king = Restaurant('Burger King', 'american')
# rest_pepperoni = Restaurant('Pepperoni', 'italian')
#
# rest_amigo.describe_restaurant()
# rest_burger_king.describe_restaurant()
# rest_pepperoni.describe_restaurant()

# rest_amigo.number_served = 5
# print(rest_amigo.number_served)
# rest_amigo.set_number_served(15)
# print(rest_amigo.number_served)
# rest_amigo.increment_number_served(18)
# print(rest_amigo.number_served)


# 9.3/9.5
class User:

    def __init__(self, first_name: str, last_name: str, sex: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.login_attempts = 3

    def describe_user(self) -> None:
        user_info = {'first_name': self.first_name, 'last_name': self.last_name, 'sex': self.sex, 'age': self.age}
        print(user_info)

    def greet_user(self) -> None:
        print(f'Hello {self.first_name} {self.last_name}!')

    def increment_login_attempts(self) -> None:
        self.login_attempts += 1

    def reset_login_attempts(self) -> None:
        self.login_attempts = 0


bob = User('Bob', 'Dyllan', 'male', 24)


# maria = User('Maria', 'Gelviatto', 'female', 18)
#
# bob.describe_user()
# bob.greet_user()
#
# maria.describe_user()
# maria.greet_user()

# print(bob.login_attempts)
# bob.increment_login_attempts()
# bob.increment_login_attempts()
# bob.increment_login_attempts()
# print(bob.login_attempts)
# bob.reset_login_attempts()
# print(bob.login_attempts)


# 9.6


class IceCreamStand(Restaurant):

    def __init__(self, favours: list):
        super().__init__(restaurant_name='IceStand', cuisine_type='IceCream')
        self.flavours = favours

    def get_flavours(self):
        print('Your ice-cream have:')
        for flavor in self.flavours:
            print(flavor)


# x = IceCreamStand(['chocolate', 'banana'])
# x.get_flavours()
# x.increment_number_served(8)
# print(x.number_served)
# print(x.restaurant_name)
# print(x.cuisine_type)

# 9.7

class Admin(User):

    def __init__(self, first_name: str, last_name: str, sex: str = None, age: int = None):
        super().__init__(first_name, last_name, sex, age)
        self.privileges = Privileges()


# y = Admin('Valera', 'Lopatin')
# y.show_privileges()
# y.add_privileges('get data user', 'can delete user')
# y.show_privileges()
# y.delete_privileges('sdasdost')
# y.show_privileges()
# y.greet_user()


# 9.8

class Privileges:

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def add_privileges(self, *privileges):
        for privilege in privileges:
            self.privileges.append(privilege)
        return self.privileges

    def delete_privileges(self, privilege):
        if privilege in self.privileges:
            self.privileges.remove(privilege)
        else:
            print('Privilege was not found')

    def show_privileges(self):
        print(f"You will be: {', '.join(self.privileges)}")

# w = Admin('Valera', 'Lopatin')
# w.privileges.show_privileges()
# w.privileges.add_privileges('qwe', 'werr')
# w.privileges.show_privileges()


# 9.13
from random import randint


class Die:

    def __init__(self, sides: int = 6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


# 9.14/9.15
from random import choice

ticket_data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'e')
count = 0
win_ticket = []
while len(win_ticket) < 4:
    win_ticket.append(str(choice(ticket_data)))
    count += 1

print(f"The ticket of winner is {win_ticket}")

my_ticket = win_ticket[:]
count_iter = 0
while len(my_ticket) > 0:
    random_value = str(choice(ticket_data))
    if random_value == my_ticket[0]:
        my_ticket.remove(random_value)
    count_iter += 1


print(count_iter)







