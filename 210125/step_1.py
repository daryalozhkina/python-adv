import timeit

name = 'иван'



alphabet = {chr(el) for el in range(ord('а'), ord('я') + 1)}
alphabet.add('ё')

# set_1 = {'а', 'б' 'в'}
# set_2 = {'а', 'б'}
#
# print(set_1 - set_2)




import timeit

to_measure_1 = '''
name = 'иван'
# alphabet = {chr(el) for el in range(ord('а'), ord('я') + 1)}
# alphabet.add('ё')
is_valid = not set(name) - alphabet
# print(is_valid)
'''

to_measure_2 = '''
name = 'иван'
# alphabet = {chr(el) for el in range(ord('а'), ord('я') + 1)}
# alphabet.add('ё')
is_valid = True
for letter in name:
   if letter not in alphabet:
    is_valid = False
    break
# print(is_valid)
'''

print(timeit.timeit(to_measure_1, number=1000000, globals={'alphabet': alphabet, 'name': name}))
print(timeit.timeit(to_measure_2, number=1000000, globals={'alphabet': alphabet, 'name': name}))

import time

alphabet = {chr(el) for el in range(ord('а'), ord('я') + 1)}
alphabet.add('ё')

start = time.perf_counter()
for _ in range(1000000):
    is_valid = not set(name) - alphabet
print(time.perf_counter() - start)

start = time.perf_counter()
for _ in range(1000000):
    is_valid =True
    for letter in name:
        if letter not in alphabet:
            is_valid = False
            break
print(time.perf_counter() - start)
