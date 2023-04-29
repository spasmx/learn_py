# 10.6
def add(a, b):
    """" add two integers """
    try:
        result = int(a) + int(b)
    except ValueError:
        print('Value must be integer')
    else:
        print(result)


# 10.7
def add_true_loop():
    print('Enter "q" for quit')
    while True:
        f_num = input('Enter first number: ')
        s_num = input('Enter second number: ')
        if f_num == 'q' or s_num == 'q':
            break
        add(f_num, s_num)


# 10.8
def reading_file(file_name):
    try:
        with open(file_name) as f:
            file = f.read()
            print(f'Program reading {file_name}\n')
            print(file)
    except FileNotFoundError:
        print(f'File {file_name} not found')


# reading_file('dogs.txt')
# reading_file('cats.txt')
# reading_file('learning_python.txt')

# 10.9
def reading_file_quiet_mode(file_name):
    try:
        with open(file_name) as f:
            file = f.read()
            print(f'Program reading {file_name}\n')
            print(file)
    except FileNotFoundError:
        pass


# reading_file_quiet_mode('dogs.txt')
# reading_file_quiet_mode('cats.txt')
# reading_file_quiet_mode('dogs.txt')

# 10.10
def word_counter(file_name, word):
    with open(file_name, encoding='utf-8') as f:
        file = f.read()
    return file.lower().count(word)


print(word_counter('Historical_Vignettes_1st_Series_by_Bernard_Capes', 'the'))



