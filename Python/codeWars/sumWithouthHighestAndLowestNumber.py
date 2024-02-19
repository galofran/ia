
"""
def sum_array(arr):
    if not arr:
        return 0

    if len(arr) <= 2:
        return 0
    else:    
        mayor = arr[0]
        menor = arr[0]
        vecesMayor = 0
        repetido = 0
        
        cont1 = 0
        while cont1 < len(arr):
            if arr[cont1] > mayor:
                mayor = arr[cont1]
                vecesMayor+=1
                if vecesMayor >= 1:
                    repetido = arr[cont1]
                    
            if arr[cont1] < menor:
                menor = arr[cont1]
            cont1+=1

        arrLimpio = []
        cont2 = 0
        while cont2 < len(arr):
            if arr[cont2] != menor and arr[cont2] != mayor:
                arrLimpio.append(arr[cont2])
            cont2+=1
        
        arrLimpio.append(repetido)
    #return arrLimpio, vecesMayor, repetido 
    return f"{arrLimpio} --- {mayor, menor} --- {sum(arrLimpio)}" 
        
print(sum_array([6, 2, 1, 8,10]))
print(sum_array([-6,-20,-1,-10,-12]))
print(sum_array([-6,20,-1,10,-12]))
"""


def sum_array(arr):
    if not arr:
        return 0

    if len(arr) <= 2:
        return 0
    else:    
        hayRepetidos = False
        valorRepetido = 0
        vecesRepetido = 0
        
        dic = dict(zip(arr,map(lambda x: arr.count(x),arr)))
   
        for x,y in dic.items():
            if y > 1:
                hayRepetidos = True
                valorRepetido = x
    
                if y >= 2:
                    vecesRepetido = y
        
        numeros = []
        maximo = max(arr)
        minimo = min(arr)
    
        if hayRepetidos:
            if vecesRepetido >= 2:
                for numero in arr:
                    if numero != maximo and numero != minimo:
                        numeros.append(numero)
                        
            if maximo == valorRepetido or minimo == valorRepetido:
                numeros.append(valorRepetido)
            
            print("Valores:",numeros,len(numeros))
        else:        
            for numero in arr:
                if numero != maximo and numero != minimo:
                    numeros.append(numero)             
        return sum(numeros)
        #return dict(zip(arr,map(lambda x: arr.count(x) > 1,arr)))
    
print(sum_array([72, -3, -1, -917, 90, 9, -527, -46, 42, 100, 69, 12, 74, -879, 3, 736, -62, -937, 1, 7, -352, 96, 10, -30, -4, 83, 45, 764, -299, -737, 921, 5, 42, -8, -834, -909, -67, 28, -8, -49, -878]))    
#print("LEN: ",len(([72, -3, -1, -917, 90, 9, -527, -46, 42, 100, 69, 12, 74, -879, 3, 736, -62, -937, 1, 7, -352, 96, 10, -30, -4, 83, 45, 764, -299, -737, 921, 5, 42, -8, -834, -909, -67, 28, -8, -49, -878])))
print(sum_array([6, 0, 1, 10,10]))

#def sum_array(arr):
#    return 0 if arr == None else sum(sorted(arr)[1:-1])
print(sum_array([72, -3, -1, -917, 90, 9, -527, -46, 42, 100, 69, 12, 74, -879, 3, 736, -62, -937, 1, 7, -352, 96, 10, -30, -4, 83, 45, 764, -299, -737, 921, 5, 42, -8, -834, -909, -67, 28, -8, -49, -878]))    
print(sum_array([6,0,1,10,10]))
print(sum_array([6, 2, 1, 8,10]))
print(sum_array([-6,-20,-1,-10,-12]))
print(sum_array([-6,20,-1,10,-12]))

"""
arr = ([72, -3, -1, -917, 90, 9, -527, -46, 42, 100, 69, 12, 74, -879, 3, 736, -62, -937, 1, 7, -352, 96, 10, -30, -4, 83, 45, 764, -299, -737, 921, 5, 42, -8, -834, -909, -67, 28, -8, -49, -878])
dic = dict(zip(arr,map(lambda x: arr.count(x),arr)))
for k,v in dic.items():
    if v > 1:
        print(f"{k}:{v}")"""
        