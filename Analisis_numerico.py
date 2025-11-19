#Solicitar tres números enteros 
a = int(input("Ingresa el primer número: ")) 
b = int(input("Ingresa el segundo número: ")) 
c = int(input("Ingresa el tercer número: ")) 
#Verificar si los tres números son positivos 
if a > 0 and b > 0 and c > 0: 
    print("Los tres números son positivos.") 
#Verificar si al menos uno es negativo 
elif a < 0 or b < 0 or c < 0: 
    print("Uno de los números es negativo.") 
#Verificar si exactamente uno es cero 
elif (a == 0 and b != 0 and c != 0) or (b == 0 and a != 0 and c != 0) or (c == 0 and a != 0 and b != 0): 
    print("Exactamente uno de los números es cero") 
#Si no entra en ninguna condición anterior: 
else: 
    print("No cumple ninguna de las condiciones específicas.")