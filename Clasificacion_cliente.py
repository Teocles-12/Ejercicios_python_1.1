monto=input("Ingrese el vlor total de la compra: " ) 
#Validación 
if monto.isdigit(): 
    monto= int(monto) 
else: 
    print("Error: el monto ingresado no es válido.") 
    exit() 
membresia= input("Ingrese el tipo de membresía (activa / temporal / ninguna): ").lower() 

if monto >= 100000 and membresia == "activa": 
    clasificacion="Premium" 
elif (50000 <= monto < 100000) or membresia == "temporal": 
    clasificacion="Frecuente" 
else: 
    clasificacion="Regular" 
print(f"Clasificación del cliente: {clasificacion}")