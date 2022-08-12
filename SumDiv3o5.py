# La funcion recibe un numero entero y devuelve la suma de todos los numeros que son
# divisibles por 3 o 5 que se encuentren debajo de este numero
def sumMultiplos3o5(num=1000):
    sum = 0
    for n in range(1, num):
        if (n%3 == 0) | (n%5 == 0):
            sum += n
            print(n)
    return print(f'La suma de todos los numeros debajo de {num} divisibles por 3 o 5 es: \n{sum}')
sumMultiplos3o5(int(input('Ingrese un numero entero:\n')))