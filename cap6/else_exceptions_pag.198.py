value = '10'
print(repr(value), 'is', end=' ')
try:
    value + 0
except TypeError:
    try:
        value + ''
    except TypeError:
        print('neither a number nor a string')
    else:
        print('some kind of string')
else:
    print('some kind of number')
