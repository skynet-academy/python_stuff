class My_decorator(object):
    """this is a class decorator"""
    def __init__(self, my_func):
        self.my_func = my_func

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.my_func.__name__))
        return self.my_func(*args, **kwargs)
def my_decorator(func):
    def wrapper_func(*args, **kwargs):
        print("I'm a wrapper function called {}, look at me".format(func.__name__))
        return func(*args, **kwargs)
    return wrapper_func


@My_decorator
def my_func():
    print('display function ran')

@my_decorator
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))






my_func()
display_info('Nicolas', 31)

