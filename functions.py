def square(x):    # f(x) ->  x*x
    return x*x

def repeat(text):
    return text * 2

def imprimir(text):
    print(text)

def cube(x):
    try:
        return x**3
    except:
        return 0

def cube2(x):
    if type(x) == int:
        return x ** 3
    else:
        return 0

def fibonacci(n):
    if n in {0, 1}:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n -  2)

def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)

def iteration_factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial * i
        #factorial *= i Esto es lo mismo de arriba
    return factorial

res = recursive_factorial(5)
print(res)
res = iteration_factorial(5)
print(res)
# res = cube2("pene") #res debe ser 0
# print(res)
# res = cube2(-2) #res debe ser -8
# print(res)

