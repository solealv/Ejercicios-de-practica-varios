# La funcion recibe un numero entero "num" y devuelve el minimo numero entero divisible por todos 
# los numeros que se encuentren en el intervalo de 1 a "num" y una lista con los numeros resultantes 
# de la factorizacion de dicho numero.

def minimoNumDivisible(num):
    multiplos = []
    minimo = 1
    for numero in range(2, num + 1):
        divisor = 2
        prueba = minimo
        while numero != 1:
            while numero%divisor == 0:
                numero /= divisor
                if prueba%divisor != 0:
                    minimo *= divisor
                    multiplos.append(divisor)
                else: prueba /= divisor
            divisor += 1
    return print(f'El minimo numero divisible por todos los numeros enteros entre 1 y {num} es: \n{minimo} \nLa lista de numeros resultantes de la factorizacion del mismo es: \n{sorted(multiplos)}')

minimoNumDivisible(int(input('Ingrese un numero entero. \nLa funcion recibe un numero entero "num". \nDevuelve el minimo numero entero divisible por todos los numeros que se encuentren \nen el intervalo de 1 a "num" y una lista con los numeros resultantes \nde la factorizacion de dicho numero.\n')))