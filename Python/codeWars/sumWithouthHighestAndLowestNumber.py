def sumArray(arr):
    if not arr:
        return 0

    if len(arr) == 0 or len(arr) == 1:
        return 0
    else:    
        maximo = max(arr)
        minimo = min(arr)
        
        numeros = []
        
        for numero in arr:
            if numero != maximo and numero != minimo:
                numeros.append(numero)

        mayor = 0
        menor = 0
        for numero in arr:
            actual = numero
            


        #print(f"Numeros: {numeros}")
        return sum(numeros)

print(sumArray([6, 0, 1, 10, 10]))