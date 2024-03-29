def regressive(n):
    print(n)
    if n > 1:
        regressive(n-1)

'''def factorial(n):
    resultado = 1
    while n > 0:
        resultado *= n
        n = n - 1
    print(resultado)'''


def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)

# regressive(5)
print(factorial(5))


def somaRecursiva(n):
    if n < 1:
        return n
    else:
        return n + somaRecursiva(n - 1)


print(somaRecursiva(5))

numero = 12
print("-----------------------")
barrabarra = numero // 10
print(barrabarra)
porcentagem = numero % 10
print(porcentagem)