import numpy as np

def prod(n, init_i, f):
        result = 1
        for i in np.linspace(init_i, init_i + n):
            result *= f(i)
        return result

def summ(n, init_i, f):
        result = 0
        for i in np.linspace(init_i, init_i + n):
            result += f(i)
        return result

I = lambda x: x

def pisigma(n, init_i, f): 
    return prod(n, init_i, f)/summ(n, init_i, f)

