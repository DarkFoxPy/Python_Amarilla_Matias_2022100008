'''
Practica sobre listas
'''

array=["futbol","Pc",18.6,18,[6,7,10.5],True,False]
print("el array contiene:",array)
#imprimir posicion 
print(array[4])
#longitud
print(len(array))
array.append(66)
print(array)


array.insert(0,88)
print(array)

array.extend([1,88,True,100])
print(array)