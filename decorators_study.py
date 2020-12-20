from functools import wraps

def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

def decorator_func(original_func):
    @wraps(original_func) # for multiple decorators
    def wrapper_func(*args, **kwargs):
        print("wrapper executed this before {}".format(wrapper_func.__name__))
        return original_func(*args, **kwargs)
    return wrapper_func

class decorator_class(object):
    def __init__(self, original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        print("call method executed this before {}".format(self.original_func.__name__))
        return self.original_func(*args, **kwargs)


def display():
    print("display function run")

@decorator_class
def decorated_display():
    print("decorated display function run")

@decorator_class
def display_info(name, age):
    print("display_info ran with arguments ({}, {})".format(name, age))

# display_info('John', 25)
# decorated_display()

# practical examples

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and Kwargs: {}'.format(args, kwargs)) 
        return orig_func(*args, **kwargs)
    return wrapper

def my_timer(orig_func):
    import time
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result
    return wrapper


@my_logger
def display_logger(name, age):
    print("display_info ran with arguments ({}, {})".format(name, age))

display_logger('John', 25)