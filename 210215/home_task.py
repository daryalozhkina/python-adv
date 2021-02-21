def my_str(str_arg):
    def the_decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f'{str_arg}\n{result}\n{str_arg}'
        return wrapper
    return the_decorator


@my_str('-')
def decorated_function(input):
    return input


print(decorated_function('Сегодня понедельник'))
