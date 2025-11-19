Restringidos=["admin","root","invitado"] 
usuario=input("Ingrese su nombre de usuario: ") 
codigo=int(input("Ingrese su código númerico: ")) 
if usuario in Restringidos: 
    print("Acceso denegado: usuario restringido") #Verificar si el usuario está en la lista restringida 
else: #Si no está en la lista restringida, revisar el código
    multiplo_2=(codigo % 2 == 0) 
    termina_7=(codigo % 10 == 7) 
    if multiplo_2 or termina_7: #Condición principal: al menos una es verdadera
        print("Acceso permitido") 
    else: 
        print("Acceso denegado: código inválido")