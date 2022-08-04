import math

def calc_plus(a, b):
    c = a + b
    return c
    pass

def calc_minus(a, b):
    c = a - b
    return c
    pass

def calc_del(a, b):
    c = a / b
    return c
    pass

def calc_mnozh(a, b):
    c = a * b
    return c
    pass

def calc_get(a, n):
    c = a ** n
    return c
    pass

def calc_square(a):
    c = a ** 2
    return c
    pass

def calc_sqrt(a):
    c = math.sqrt(a)
    return c
    pass

def calc_sin(x):
    '''
    calc_sin(30) = 0.5
    для перевода градусов в радианы можете использовать math.radians()
    '''
    c = math.sin(math.radians(x))
    return round(c, 3)
    pass

def calc_cos(x):
    c = math.cos(math.radians(x))
    return round(c, 2)
    pass

def calc_tg(x):
    '''
    для несуществующих тангенсов (90, 270 ...)
    выводите None
    '''
    if (x+90) % 180 == 0:
        return None
    else:
        c = math.tan(math.radians(x))
        return round(c)
    pass

def calc_ctg(x):
    if calc_sin(math.radians(x)) == 0:
        return None
    else:
        c = 1 / (math.tan(math.radians(x)))
        return round(c)
    pass

if __name__=="__main__":
    print(calc_sin(30))
