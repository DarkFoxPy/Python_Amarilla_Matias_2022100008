'''
Crear un programa que pida dos numero y obtenga como resultado
cual de ellos es par o si ambos lo son
'''
numero1=int(input("Ingrese primer numero: "))
numero2=int(input("Ingrese segundo numero: "))

if((numero1%2==0) and(numero2%2==0)):
    print("los numeros ",numero1 , "y", numero2, " son pares")
elif ((numero1%2==0) and (numero2%2!=0)):
    print("El numero ",numero1, "es par, y el numero ", numero2, "es impar")
elif ((numero1%2!=0) and (numero2%2==0)):
    print("El numero ",numero2, "es par, y el numero ", numero1, "es impar")
else:
    print("los numeros ",numero1 , "y", numero2, " son impares")