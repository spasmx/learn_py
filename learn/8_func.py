# # 8.1
# def display_message():
#     print('This block about function')
#
#
# display_message()
#
#
# # 8.2
# def favorite_book(title):
#     print(f'My favorite book is {title.title()}')
#
#
# favorite_book('book')
#
#
# # 8.3
# def make_shirt(size, print_text):
#     print(f'Size shirt - {size}\nText when will be print on shirt - {print_text}')
#
#
# make_shirt('L', 'Hello World!')
# make_shirt(print_text='Hello World!', size='L')
#
#
# # 8.4
# def make_shirt_(size='L', print_text='I love Python'):
#     print(f'Size shirt - {size}\nText when will be print on shirt - {print_text}')
#
#
# make_shirt_()
# make_shirt_('M')
# make_shirt_('S', 'Hello World!')
#
#
# # 8.5
# def describe_city(city: str, country='Ukraine'):
#     print(f'{city.title()} is in {country.title()}')
#
#
# describe_city('Kyiv')
# describe_city('New York', 'usa')
# describe_city('krakow', 'poland')
#
#
# # 8.6
# def city_country(city, country):
#     return f'{city.title()}, {country.title()}'
#
#
# print(city_country('kyiv', 'ua'))
# print(city_country('london', 'en'))
# print(city_country('warsawa', 'pl'))
#
#
# # 8.7
# def make_album(artist, album, count_song=None):
#     music_info = {'artist': artist.title(), 'album': album.title()}
#     if count_song:
#         music_info['count_song'] = count_song
#     return music_info
#
#
# print(make_album('lorna shore', 'pain remains'))
# print(make_album('lifelover', 'pulver'))
# print(make_album('ghost bath', 'funeral', 12))
#
# # 8.8
# while True:
#     print('\nEnter artist and album')
#     artist = input('Enter artist: ')
#     album = input('Enter album: ')
#     music_list = make_album(artist, album)
#     print(music_list)
#     repeat = input('\nWould you like repeat y/n: ')
#     if repeat == 'n' or repeat == 'N':
#         break


# 8.9
def show_messages(msgs):
    for msg in msgs:
        print(msg)


messages = ['a', 'b', 'c', 'd']
show_messages(messages)


# 8.10
def send_messages(msgs):
    sent_messages = []
    while msgs:
        msg = msgs.pop(0)
        print(msg)
        sent_messages.append(msg)
    return sent_messages


x = send_messages(messages)
print(messages, x)


# 8.11
messages = ['a', 'b', 'c', 'd']
print(messages, send_messages(messages[:]))


# 8.12
def make_sandwich(*args):
    print(f'Your sandwich with: {", ".join(args)}')


make_sandwich('tomato')
make_sandwich('meat', 'tomato')
make_sandwich('pepperoni', 'cheese', 'tomato', 'meat-bowl')


# 8.13
def build_profile(f_name, l_name, **kwargs):
    kwargs['first_name'] = f_name
    kwargs['last_name'] = l_name
    return kwargs


my_profile = build_profile('Maksym', 'Maksym', country='Ukraine', city='Kyiv', position='QA')
print(my_profile)


# 8.14
def make_car(car, model, **kwargs):
    kwargs['car'] = car
    kwargs['model'] = model
    return kwargs


car_info = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car_info)








