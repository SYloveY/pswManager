from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)'''


def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open('db.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split('||')
            print('User:', user, ', Password:', fer.decrypt(pwd.encode()).decode())


def add():
    login = input('Введите логин аккаунта: ')
    password = input('Введите пароль: ')

    with open('db.txt', 'a') as f:
        f.write(login + ' || ' + fer.encrypt(password.encode()).decode() + '\n')


while True:
    mode = input('Хотите добавить новый пароль, или просмотреть готовый вариант(добавить, просмотреть)?'
                 'Для выхода нажмите "q" ').lower()
    if mode.lower() == 'просмотреть':
        view()
    elif mode.lower() == 'добавить':
        add()
    elif mode.lower() == 'q':
        break
    else:
        print('Упс, нету такого варианта :(')
        continue
