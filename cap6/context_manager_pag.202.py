import contextlib


@contextlib.contextmanager
def enclosing_tag(tagname):
    print(f'<{tagname}>', end='')
    try:
        print("I'll stay here until...")
        yield
    finally:
        print(".. I'll have completed")
        print(f'</{tagname}>')


with enclosing_tag('mot'):
    for i in ['hello', 'world', 'complex']:
        print(i)
