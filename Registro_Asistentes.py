nombres=[] #Lista donde se guardaran todos los nombres ingresados
entrada=input("Ingresa un nombre (o 'FIN' para terminar): ") #Primera lectura antes del ciclo
entrada=entrada.strip() 
while entrada.upper() != "FIN": #Ciclo controlado por la condición: continúa mientras no sea FIN
    if entrada == "": #Ignorar entradas vacías
        print("Entrada vacía. Intenta nuevamente.") 
    else: 
        nombres.append(entrada) #Guardar el nombre válido 
    
    #Leer nuevamente para continuar el ciclo 
    entrada=input("Ingresa un nombre (o 'FIN' para terminar): ") 
    entrada=entrada.strip() 
print("\nTotal de nombres ingresados:", len(nombres)) #Mostrar el total de nombres ingresados 
repetidos=False #Detectar si hay nombres repetidos
for nombre in nombres:  
    if nombres.count(nombre) > 1:
        repetidos=True 
        break 
#Resultado final
if repetidos: 
    print("Hay nombres repetidos.") 
else: 
    print("No hay nombres repetidos.")
