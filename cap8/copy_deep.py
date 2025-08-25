import copy
def copyjhonny(a,b,c,d):
    a[0].append(1)
    b[0].append(2)
    c[0].append(3)
    d[0].append(4)


ll = [[]]
a = ll
b = ll[:]
c = copy.copy(ll)
d = copy.deepcopy(ll)

copyjhonny(a, b, c, d)
print(a, b, c, d)
           
