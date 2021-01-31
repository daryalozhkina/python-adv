

alphabet = {chr(el) for el in range(ord('а'), ord('я') + 1)}

alphabet.update(['ё', '-'])




def name_is_valid(name):
    if not name or set(name.lower()) - alphabet:
        return False
    if '-' in name:
        for _name in name.split('-'):
            if not _name.istitle():
                return False
            return True
    return name.istitle()


print(name_is_valid('иван'))
print(name_is_valid('Иван'))
print(name_is_valid('Анна-Виктория'))
