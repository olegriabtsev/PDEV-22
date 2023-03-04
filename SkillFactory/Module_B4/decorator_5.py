USERS = ['admin', 'guest', 'director', 'root', 'superstar']

yes_no = input("""Введите Y, если хотите авторизоваться, или N, 
             если хотите продолжить работу как анонимный пользователь: """)

auth = yes_no == 'Y'


def is_auth(func):
    def wrapper():
        if auth:
            print('Пользователь авторизован')
            func()
        else:
            print('Пользователь не авторизован. Функция выполнена не будет')

    return wrapper


def has_access(func):
    username = input('Введите username: ')

    def wrapper():
        if username in USERS:
            print('Такой пользователь существует', username)
            func()
        else:
            print('Такого пользователя не существует', username)

    return wrapper


@is_auth
@has_access
def from_db():
    print('some data from database')


from_db()
