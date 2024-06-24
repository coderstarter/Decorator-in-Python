logged_in_user = None


def authenticate(func):
    print(func.__name__)
    def wrapper(username):
        print(username)
        if logged_in_user is None:
            print('Authentication failed!!')
            return  None
        else:
            return func(username)
    return wrapper
@authenticate
def check(name):
    print('details user logged in : ', name)

logged_in_user = None
check('root')
