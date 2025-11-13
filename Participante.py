edad=int(input("Digita tu edad: "))  

if edad <= 0: 
    print("Edad no válida") 
elif edad <=17: 
    print("Lo siento no tienes la edad requerida.")
else:  
    if edad >= 18: 
        print("Debe presentar su documento de identidad.") 
    documento=input("¿Puedo ver su documentación? (Si/no): ").lower()

    if documento == "si": 
        print("Comprobado,es mayor de edad.")  
    elif documento == "no":
        print("Lo sentimos no puedes continuar con el proceso.") 

    Vehiculo_propio="1" 
    Vehiculo_autorizado="2" 
    Tipo_Vehiculo=input(""" 
                        ¿Qué tipo de vehículo usas?  
                        
                        Vehículo propio: 1 
                        Vehículo autorizado: 2  
                    -Digita una opción: """).isalpha()

    Licencia=input("¿Tiene licencia de condución? (Si/no): ").lower()  
    if Licencia == "no": 
        print("Debe hacer el tramite para obtener una licencia.") 
    elif Licencia == "si":
        vigencia=input("¿Está aún vigente? (Si/no): ").lower()
        if Licencia == "si" and vigencia == "si": 
            print("Gracias por la comprobació de licencia.") 
        elif Licencia == "si" and vigencia == "no":   
            print("Debe hacer el tramite para hacer la vigencia de la licencia.") 
    
    if Vehiculo_propio == "1" and Licencia == "si" and vigencia == "si": 
        print("Eres Apto.") 
    #elif Vehiculo_autorizado 
        

