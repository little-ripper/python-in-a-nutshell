def announce(f):
    def wrap(*a, **k):
        print(f'Calling {f.__name__}')
        print(a[:])
        for value in k.values():
            print(value)
        return f(*a, **k)
    return wrap


@announce
def function_test(a=[], b={}):
    print(f"inside at this {function_test.__name__}")
## This is the same as this:
## function_test = announce(function_test)

## I calling with arguments
function_test([1,2,3], {"ky0": 0, "ky1": 1})
print(type(function_test))
print(type(announce))
## OUTPUT
# Calling function
# ([1, 2, 3], {'ky0': 0, 'ky1': 1})
# inside at this wrap
# <class 'function'>
# <class 'function'>
# >>> 

## observe the differences
# @announce
def function_another(a=[], b={}):
    print(f"inside at this {function_another.__name__}")
## This is the same as this:
fun = announce(function_another)

## I calling with arguments
fun([1,2,3], {"ky0": 0, "ky1": 1})
print(type(fun))
print(type(announce))
## OUTPUT
# Calling function_another
# ([1, 2, 3], {'ky0': 0, 'ky1': 1})
# inside at this function_another
# <class 'function'>
# <class 'function'>
# >>> 
