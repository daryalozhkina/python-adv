import re

RE_FLOAT_VALIDATOR = re.compile(r'^[0-9]?(?:\.,\d*)?\d+')


def float_is_valid(float):
    return RE_FLOAT_VALIDATOR.match(float)


assert float_is_valid('1.25')
assert float_is_valid('1,25')
assert not float_is_valid('13')
assert not float_is_valid('-12')