#Usuario predefinido 
Usuario_correcto="usuario1" 
Contraseña_correcta="password123" 
Max_intentos=3 
intentos_validados=0 
acceso_permitido=False 
#Bucle principal: se repite mientras no haya acceso y queden intentos válidos por consumir 
while intentos_validados < Max_intentos and not acceso_permitido: 
    usuario=input("Usuario: ").strip() #Pedir al usuario: contraseña y usuario
    contrasena=input("Contraseña: ").strip() 
    if usuario == "" and contrasena == "": #Caso especial: ambos campos vacíos -> no cuenta como intento
        print("No ingresaste usuario ni contraseña - este intento NO cuenta.") 
        continue #Continue: vuelve al inicio del while sin aumentar intentos_validados
    intentos_validados += 1 #Al llegar acá, el intento sí cuenta
    intent_actual = intentos_validados #Para mostrar en mensajes
    usuario_ok=(usuario==Usuario_correcto) #Evaluación completa de los posibles fallos y éxito
    contrasena_ok=(contrasena==Contraseña_correcta) 
    if usuario_ok and contrasena_ok: #Si ambas son correctas -> acceso
        print(f"Acceso permitido. Bienvenido/a, {usuario}.") 
        acceso_permitido=True 
        break  
        #Si no, mostrar motivos detallados     
    if not usuario_ok and not contrasena_ok: #Caso: ambos incorrectos (o no coinciden)
        if usuario == "" and contrasena == "": #Distinguimos si alguno está vacío para dar un mensaje más claro
            motivo="ninguno ingresado" #(no debería ocurrir por el continue anterior, pero uqeda en la comprobación)
        elif usuario == "": 
            motivo="usuario vacío y contraseña incorrecta" 
        elif contrasena == "": 
            motivo="contraseña vacía y usuario incorrecto" 
        else: 
            motivo="usuario y contraseña incorrectos" 
        print(f"Intento {intent_actual}/{Max_intentos}: Acceso denegado - {motivo}.")  
    #Caso: usuario incorrecto, contraseña correcta 
    elif not usuario_ok and not contrasena_ok: 
        if usuario == "":
            motivo="usuario vacío" 
        else: 
            motivo="usuario incorrecto" 
        print(f"Intento {intent_actual}/{Max_intentos}: Acceso denegado - {motivo}.")  
    #Caso: usuario correcto, contraseña incorrecta    
    elif usuario_ok and not contrasena_ok: 
        if contrasena == "": 
            motivo="contraseña vacía" 
        else: 
            motivo="contraseña incorrecta" 
        print(f"Intento {intent_actual}/{Max_intentos}: Acceso denegado - {motivo}")
if not acceso_permitido: #Fin del bucle: informamos resultado final
    print("Se alcanzó el máximo de intentos. Acceso bloqueado.")