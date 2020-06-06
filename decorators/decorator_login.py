def my_logger(func):
    import logging
    logging.basicConfig(filename='{}.log'.format(func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
    return func(*args, **kwargs)

    return wrapper

def my_timer(func):
    import time 
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(func.__name__, t2))
        return result

    return wrapper


import time 

@my_timer
def func(name, age):
    print('{} ran with arguments({}, {})'.format(func.__name__, name, age))

func('Nicolas', 31)

