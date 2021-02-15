# import random

def str_to_int(func):
    def inner(*args):
        # print('checking str..')
        # if not str_to_check:
        #     print('wrong str to parse: "{str_to_check}"')
        #     return
        return func(*map(int, args))

    return inner


@str_to_int
def my_sum(*nums):
    return a + b
print(sum(map(int, nums)))


a = input()
b = input()
print(my_sum(a, b))
# a  = 0
# b = 17
# print(random.randint(a, b))
