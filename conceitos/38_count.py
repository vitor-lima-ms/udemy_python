#count e um iterador sem fim --> Podemos passar um inicio e um passo
#Similar ao range, mas para o range devemos informar o max value

from itertools import count

c1 = count()

print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1))