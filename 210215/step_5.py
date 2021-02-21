# import random

def str_to_int(func):
    def inner(*args):
        # print('checking str..')
        # if not str_to_check:
        #     print('wrong str to parse: "{str_to_check}"')
        #     return
        return func(*map(int, args))

    return inner

def str_to_float(func):
    def inner(*args):
        return func(*map(float, args))

    return inner

@str_to_float
def nums_sum(*nums):
    return sum( nums)

#
# a = input()
# b = input()
# print(my_sum(a, b))
# a  = 0
# b = 17
# print(random.randint(a, b))

print(nums_sum(2, 3))
print(nums_sum(2.3, 3.5))
# a = input()
# b = input()
# print(my_sum(a, b))
print(nums_sum('2', '3'))
print(nums_sum('2.3', '3.5'))