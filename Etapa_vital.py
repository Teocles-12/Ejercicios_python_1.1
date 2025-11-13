#Datos del usuario  
edad=int(input("Digite su edad: "))  
#Validar las condiciones 
if edad <= 0: 
    print("Bro, estas seguro que acabaste de nacer o te estas convirtiendo en espermatoziode.") 
elif edad >= 1 and edad <= 6: 
    print("Su nivel educativo es Infante. Juega y disfruta.") 
elif edad >= 7 and edad <= 17:
    print("Su nivel educativo es Estudiante escolar. Haz amigos, y aprende los conocimientos básicos de las personas.") 
elif edad >= 18 and edad <= 25: 
    print("Su nivel educativo es Universitario. Es hora de ver que camino tomarás, no te olvides de disfrutar la juventud.") 
elif edad >= 26 and edad <= 59: 
    print("Su nivel educativo es Adulto activo. Eres adulto responsable y maduro, eso espero.") 
elif edad >= 60: 
    print("Su nivel educativo es Adulto mayor jubilado. Recuerda que llego la hora de disfrutar lo que queda de vida con las personas que fuistes creando en el camino.") 
else: 
    print("No determinado")