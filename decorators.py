import functools

def my_decorator(func):
    @functools.wraps(func)

    def function_that_runs_fun():
        print('in the decorator')
        func()
        print('after the decorator')

    return function_that_runs_fun

@my_decorator
def my_function():
    print('im the function')

my_function()

##

def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_fun(*args, **kwargs):
            print('Im the decorator')
            if number == 56:
                print('Not running the function')
            else:
                func(*args, **kwargs)
            print('After the decorator')
        return function_that_runs_fun
    return my_decorator

@decorator_with_arguments(56)
def my_function_too(x, y):
    print(x + y)

my_function_too(55,55)