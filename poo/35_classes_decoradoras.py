#Decoram objetos

class Multiply:
    def __init__(self, multiplier):
        self.multiplier = multiplier
    
    def __call__(self, func):
        def inner(*args, **kwargs):
            result = func(*args) * self.multiplier
            return result
        return inner

@Multiply(10)
def my_sum(*args):
    sum_ = 0
    for arg in args:
        sum_ += arg
    return sum_ #Ou simplesmente sum(args)

result = my_sum(1, 2, 3)
print(result)