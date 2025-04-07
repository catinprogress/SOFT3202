# coverage run -m pytest filename.py
# coverage report -m
# coverage html 
def add(xs):
    result = 0
    for x in xs:
        result += x
    return result

assert add([]) == 0
assert add([1]) == 1