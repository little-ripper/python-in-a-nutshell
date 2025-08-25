class Bunch:
    def __init__(self, **fields):
        self.__dict__ = fields
p = Bunch(x=2.3, y=4.5)
print(p)

class Point(Bunch):
    x = 0.0
    y = 0.0
    color = 'gray'
p = Point()
print(p)
p = Point(x=1.2, y=3.4)
print(p)

import warnings

class MetaBunch(type):

    def __new__(mcl, classname, bases, classdict):
        def __init__(self, **kw):
            for k in self.__dflts__:
                if not k in kw:
                    setattr(self, k, self.__dflts__[k])
            for k in kw:
                setattr(self, k, kw[k])
        def __repr__(self):
            rep = [f'{k}={getattr(self, k)!r}' for k in self.__dflts__ if getattr(self, k) != self.__dflts__[k]]
            return f'{classname}({", ".join(rep)})'
        newdict = {'__slots__': [], '__dflts__': {}, '__init__': __init__, '__repr__': __repr__}
        for k in classdict:
            if k.startswith('__') and k.endswith('__'):
                if k in newdict:
                    warnings.warn(f'Cannot set attr {k!r} in bunch-class {classname!r}')
                else:
                    newdict[k] = classdict[k]
            else:
                newdict['__slots__'].append(k)
                newdict['__dflts__'][k] = classdict[k]
        return super().__new__(mcl, classname, bases, newdict)

class Bunch(metaclass=MetaBunch):
    pass

class AnotherPoint(Bunch):
    x = 0.0
    y = 0.0
    color = 'gray'
ap = AnotherPoint()
print(ap)
print(ap.x)
print(ap.y)
ap = AnotherPoint(x=1.2, y=3.4)
print(ap)
ap = AnotherPoint(x=2, y=4.10)
print(ap)
print(ap.y)
print(ap.x)
