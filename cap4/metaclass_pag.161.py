class MyMeta(type):
    def __str__(self):
        return f'Beautiful class {self.__name__!r}'
class MyClass(metaclass=MyMeta):
    pass
x = MyClass()
print(type(x))
type(3)
class MyClass1(MyMeta):
    pass
y = MyClass1()
print(type(y))
