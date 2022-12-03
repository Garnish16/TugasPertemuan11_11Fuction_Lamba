import math
#GARNISH ANDHIKA PRATAMA T2.22.B1


def a(n): return lambda x: x**n


lambdaA = a(4)
print(lambdaA(4))


def b(i, j):
    return lambda x, y: math.sqrt(x**i + y**j)


lambdaB = b(4, 0)
print(lambdaB(3, 0))


def c(*args):
    return lambda *params: sum(args) / len(params)


lambdaC = c(1, 2, 3, 4, 5)
print(lambdaC(2, 2, 5))


def d(fistname):
    return lambda *lastname: "".join(set(fistname)) + "".join(set(lastname))


lambdaD = d("GARNISH")
print(lambdaD("GARNISH", "ANDHIKA"))