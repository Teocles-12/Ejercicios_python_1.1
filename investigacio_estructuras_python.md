                                      LISTAS 
->¿Qué son?  

Las listas en python son colecciones ordenadas de elementos (números, texto, booleanos,etc.)que pueden cambiarse despues de su creación.También podríamos llamarlas como un tipo de estructura de datos en Python que permite almacenar varios valores dentro de una sola variable. 
Se podría decir que es como una caja con compartimentos, donde cada compartimento guarda un valor,y cada valor tiene una posición(índice). 

EJEMPLO: Visual 

Indice       0          1            2 
------------------------------------------
Valor    "manzana"   "banana"     "pera" 

En Python, esa lista se escribe así: 
frutas=["manzana", "banana", "pera"] 

--> Características principales  

1.ORDENADAS: Los elementos tienen un opden fijo(Posición 0,1,2...). 
Si agregas nuevos elementos, se añaden al final(a menos de que se use un método para insertarlos en otro lugar).  

2.MUTABLES: Puedes modificar, agregar o eliminar elementos después de haber creado la lista.Esta es una diferencia importante con las tuplas, que son inmutables. 

3.HETEROGENEAS(Heterogéneas): Pueden contener distintos tipos de datos de datos al mismo tiempo: números, texto, booleanos, incluso otras listas. 
EJEMPLO: datos=["Ana", 25, True, 3.14] 

4.DINAMICAS(Dinámicas): No necesitas decirle al programa cuántos elementos tendrá; puedes ir agregando o quitando según lo necesites. 

---> ¿Por qué se dice que son "mutables"? 
"Mutable" significa que puedes cambiar el contenido de la lista sin crear una nueva. 
EJEMPLO: numeros=[10,20,30] 
numeros[1]=25 
print(numeros) 
#Resultado: [10,25,30] 
Aquí no se creó una lista nueva; simplemente se modificó la existente. Esa capacidad de "mutar" (Cambiar su contenido) es lo que las hace mutables. 
 
----> Cómo accede a los elementos 
Cada elemento tiene un índice (posición) que comienza en 0. 
EJEMPLO: Demostrativo 
frutas = ["manzana", "banana", "pera"] 
print(frutas[0]) # Muestra "manzana" 
print(frutas[2]) # Muestra "pera" 
También se pueden usar índices negativos: 
-1(Menos uno) útimo elemento 
-2(Menos dos) penúltimo elemento 
print(frutas[-1]) # Muestra "pera" 

-----> Cómo recorrer una lista 
A menudo se usa un bucle "for" para ver todos los elementos: 
EJEMPLO: Demostrativo 
for fruta in frutas: 
    print(fruta) 
Resultado: 
manzana 
banana 
pera 
Aquí, fruta es una variable temporal que va tomando cada valor de la lista uno por uno.  

------> Métodos importantes de las listas  

Método             |Descripción                      |Ejemplo  
-------------------------------------------------------------------------------
append(valor)      |Agrega un elemento al final      |frutas.append("uva") 
-------------------------------------------------------------------------------
insert(pos,valor)  |Inserta en una posición          |frutas.insert(1,naranja) 
                    específica 
-------------------------------------------------------------------------------
remove(valor)      |Elimina la primera aparición     |frutas.remove("banana")
                    de un indice 
-------------------------------------------------------------------------------
pop(pos)           |Elimina un elemento por índice   |frutas.pop(0) 
-------------------------------------------------------------------------------
len(lista)         |Devuelve la cantidad de          |len(frutas)
                    elementos 
-------------------------------------------------------------------------------
sort()             |Ordena los elementos si son      |numeros.sort() 
                    comparables 
------------------------------------------------------------------------------- 
reverse()          |Invierte el orden de los         |frutas.reverse()
                    elementos 

EJEMPLO: Demostrativo 
# Crear una lista con nombres
nombres = ["Ana", "Luis", "María"]

# Mostrar la lista completa
print("Lista inicial:", nombres)

# Acceder a un elemento específico
print("Primer nombre:", nombres[0])

# Modificar un elemento
nombres[1] = "Carlos"
print("Después de modificar:", nombres)

# Agregar un nuevo elemento
nombres.append("Sofía")
print("Después de agregar:", nombres)

# Insertar un elemento en una posición concreta
nombres.insert(1, "Jorge")
print("Después de insertar:", nombres)

# Eliminar un elemento por su nombre
nombres.remove("Ana")
print("Después de eliminar:", nombres)

# Ver el tamaño de la lista
print("Número de elementos:", len(nombres))

# Recorrer la lista
for nombre in nombres:
    print("Nombre:", nombre) 

Resultado: 
Lista inicial: ['Ana', 'Luis', 'María']
Primer nombre: Ana
Después de modificar: ['Ana', 'Carlos', 'María']
Después de agregar: ['Ana', 'Carlos', 'María', 'Sofía']
Después de insertar: ['Ana', 'Jorge', 'Carlos', 'María', 'Sofía']
Después de eliminar: ['Jorge', 'Carlos', 'María', 'Sofía']
Número de elementos: 4
Nombre: Jorge
Nombre: Carlos
Nombre: María
Nombre: Sofía

-------> Casos donde se usan listas en la práctica 
1.Guardar datos de usuarios 
    usuarios = ["Mateo", "Laura", "Andrés"] 

2.Almacenear calificaciones y calcular promedio 
    notas = [4.5, 3.8, 5.0] 
    promedio = sum(notas) / len(notas) 

3.Guardar objetos o registros(Listas dentro de listas) 
    productos = [ 
        ["Lápiz", 500] 
        ["Cuaderno", 2500] 
        ["Borrador", 800]
    ] 

4.Trabajar con datos dinámicos (agregar o eliminar elementos según el usuario o el programa). 

                                        TUPLAS 
->¿Qué son? 

Una tupla es una estructura de datos en Python que permite almacenar varios valores, igual que una lista, pero con una diferencia esencial: 

A.Una tupla es INMUTABLE: Esto significa que no se puede modificar después de crearla. 
*No se puede agregar elementos 
*No se puede eliminar elementos 
*No se puede cambiar un elemento por otro 

-->Sintaxis básica 
Se escribe usando paréntesis(): 
    colores = ("rojo", "verde", "azul") 
También puede crearse sin paréntesis(Python lo interpreta como tupla): 
    dias = "lunes", "martes", "miércoles"
Y si quieres una tupla de un solo elemento, debe terminar con coma, de lo contrario Python no la detecta como tupla: 
    tupla1 = (5)      # Esto es un número
    tupla2 = (5,)     # Esto sí es una tupla con un solo elemento 

--->¿Por qué son inmutables? 
Las tuplas fueron diseñadas para representar datos que NO deben cambiar, como: 
*Coordenadas 
*Fechas 
*Configuraciones 
*Constantes 
*Claves en diccionarios 
Razones técnicas: 
1.Protegen datos importantes contra modificadores accidentales. 
2.Son más rápidas que las listas. 
3.Son más seguras cuando se usasn en estructuras complejas. 
4.Al no modificarse, Python puede optimizar su uso en memoria. 

---->¿Para qué se usan las tuplas? 
1.Cuando quieres asegurarte de que los valores no cambien 
    EJEMPLO: Coordenadas o posiciones: 
    posicion = (10.5, 22.3) 
2.Cuando quieres un conjunto de opciones fijas 
    EJEMPLO: 
    dias_semana = ("lunes", "martes", "miércoles", "jueves", "viernes")
3.Cuando necesitas usar datos como clave en un diccionario 
    EJEMPLO: Python no permite que una lista sea clave porque es mutable, pero una tupla sí: 
    edades = {
    ("Juan", "Pérez"): 25,
    ("Ana", "Gómez"): 30
    } 
4.Son más rápidas que las listas 
Si solo necesitas datos de consulta, usar tuplas mejora el rendimiento. 

----->¿Cómo acceder a los elementos de una tupla? 
Exactamente igual que las listas, usando índices.  
    EJEMPLO: Demostrativo 
    frutas = ("manzana", "pera", "uva")
    print(frutas[0])  # manzana
    print(frutas[2])  # uva 
índices negativos también funcionan: 
    print(frutas[-1])  # uva (último)

------>¿Cómo se recorre una tupla? 
Igual que las listas, con un "for": 
    EJEMPLO: demostrativo 
    for fruta in frutas:
    print(fruta)
Resultado: 
    manzana
    pera
    uva 

------->Operaciones permitidas con tuplas 
Aunque no se pueden modificar,sí se puede: 
1.Obtener su longitud: 
    len(frutas) 
2.Contar cuántas veces aparece un elemento: 
    frutas.count("pera") 
3.Saber el índice de un elemento: 
    frutas.index("uva") 
4.Concatenarlas: 
    nueva = frutas + ("mango",)
5.Repetir sus elementos: 
    repetida = frutas * 2

EJEMPLO: Explicativo-Aplicativo 

# Crear una tupla
estudiante = ("Mateo", 18, "Python")

# Acceder a elementos
print("Nombre:", estudiante[0])
print("Edad:", estudiante[1])

# Recorrer la tupla
for dato in estudiante:
    print("Dato:", dato)

# Métodos disponibles
print("Cantidad de elementos:", len(estudiante))
print("Veces que aparece 'Python':", estudiante.count("Python"))
print("Índice del curso:", estudiante.index("Python"))

# Concatenar tuplas
nueva_tupla = estudiante + ("Colombia",)
print("Tupla extendida:", nueva_tupla)

SALIDA: 

Nombre: Mateo
Edad: 18
Dato: Mateo
Dato: 18
Dato: Python
Cantidad de elementos: 3
Veces que aparece 'Python': 1
Índice del curso: 2
Tupla extendida: ('Mateo', 18, 'Python', 'Colombia') 

                                    DICCIONARIOS 
->¿Qué es un diccionario? 
Un diccionario es uan estructura de datos en Python que almacena información en pares clave-valor. 
La idea es: 
*Clave : el identificador 
*Valor . la información asociada a esa clave 
    EJEMPLO: Visual 
Clave                   Valor  
--------------------------------
"nombre"                "Mateo" 
-------------------------------- 
"edad"                  18 
-------------------------------- 
"curso"                 "Python" 

En código: 
    estudiante = {
    "nombre": "Mateo",
    "edad": 18,
    "curso": "Python"
    }

-->¿Cómo almacenan la información? 
Los diccionarios no usan índices númericos como listas o tuplas. 
Usan claves, y cada clave apunta directamente a un valor.  
Internamente: 
*Python usa una estructura llamada hash table. 
*Esto permite buscar datos muy rápido, incluso en diccionarios grandes 
*Por eso acceder a algo como diccionario["nombre"] es muy eficiente 

--->Diferencias clave frente a listas y tuplas 

Característica         |Lista           |Tupla         |Diccionario 
---------------------------------------------------------------------------
Símbolo                |[]              |()            |{}  
---------------------------------------------------------------------------
Acceso                 |Por índice      |Por índice    |Por clave 
---------------------------------------------------------------------------
Mutabilidad            |Sí              |No            |Sí 
---------------------------------------------------------------------------
Tipos de datos         |Secuencia       |Secuencia     |Conjunto de pares 
                        ordenada         fija           clave-valor 
---------------------------------------------------------------------------
Claves repetidas       |No aplica       |No aplica     |No se  
                                                        permiten 
---------------------------------------------------------------------------
Orden                  |Ordenadas       |Ordenadas     |Mantienen
                                                        orden de inserción 
---------------------------------------------------------------------------         Uso típico             |Datos que       |Datos fijos   |Datos con significado
                        cambian                         (atríbutos,registros,       
                                                         objetos)

Fun fact: Los diccionarios son ideales cuando quieres asociar un valor a un nombre, no a una posición. 

---->¿Para qué se usan los diccionarios? 
Son extremadamente útiles para representar entidades con atríbutos. 
EJEMPLO: 
*Objetos del mundo real: 
    persona = {
    "nombre": "Mateo",
    "edad": 18,
    "ciudad": "Medellín"
    } 
*Inventarios: 
    inventario = {
    "manzanas": 10,
    "peras": 5,
    "bananos": 20
    } 
*Registros(como filas de bases de datos) 
    producto = {
    "id": 124,
    "nombre": "Teclado",
    "precio": 75000
    } 
*Traducciones, configuración, estadísticas, JSON, APIs... 
    Son una de las estructuras más usadas en programación real. 

----->Operaciones básicas 
Aquí lo importante es agregar, consultar, modificar, y eliminar. 
1.AGREGAR 
    estudiante["nota"] = 4.5
2.CONSULTAR ELEMENTOS 
    print(estudiante["nombre"]) 
    *Si la clave no existe, falla. 
    para evitar error: 
        print(estudiante.get("telefono", "No registrado"))
3.MODIFICAR ELEMENTOS 
    estudiante["edad"] = 19
4.ELIMINAR ELEMENTOS 
    del estudiante["curso"]
O usar: 
    estudiante.pop("edad")

------>Métodos importantes del diccionario 

| Método      | ¿Qué hace?                          |
| ----------- | ----------------------------------- |
| `.keys()`   | Devuelve todas las claves           |
| `.values()` | Devuelve todos los valores          |
| `.items()`  | Devuelve pares (clave, valor)       |
| `.get()`    | Consulta segura                     |
| `.pop()`    | Elimina por clave                   |
| `.clear()`  | Vacía todo el diccionario           |
| `.update()` | Actualiza o agrega varios elementos |
 
------->Recorrer un diccionario 
*Recorrer claves: 
    for clave in estudiante:
    print(clave)
*Recorrer solo valores: 
    for valor in estudiante.values():
    print(valor)
*Recorrer pares clave-valor 
    for clave, valor in estudiante.items():
    print(clave, "=>", valor)
 
EJEMPLO: Demostrativo 

# Crear un diccionario
persona = {
    "nombre": "Mateo",
    "edad": 18,
    "ciudad": "Medellín"
}

# Consultar un valor
print("Nombre:", persona["nombre"])

# Agregar un nuevo dato
persona["profesion"] = "Estudiante"
print("Después de agregar:", persona)

# Modificar un dato
persona["edad"] = 19
print("Después de modificar edad:", persona)

# Eliminar un dato
persona.pop("ciudad")
print("Después de eliminar ciudad:", persona)

# Recorrer el diccionario completo
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

Resultado: 

Nombre: Mateo
Después de agregar: {'nombre': 'Mateo', 'edad': 18, 'ciudad': 'Medellín', 'profesion': 'Estudiante'}
Después de modificar edad: {'nombre': 'Mateo', 'edad': 19, 'ciudad': 'Medellín', 'profesion': 'Estudiante'}
Después de eliminar ciudad: {'nombre': 'Mateo', 'edad': 19, 'profesion': 'Estudiante'}
nombre: Mateo
edad: 19
profesion: Estudiante
 
                               MATCH-CASE 
->¿Qué es? 
Es una estructura de control que permite comparar un valor con varios patrones posibles de forma más clara y ordenada que múltiples "if-elif" 

-->¿Para qué se usa? 
Para tomar decisiones según el valor de una variable o estructura, evitando el exceso de condiciones if y mejorando la legibilidad. 

--->Diferencias frente a IF y ELIF 

Característica        if/elif                 match-case 
--------------------------------------------------------------------------
Comparación           Evalúa condiciones      comapara patrones o valores 
                      lógicas                 directos 
-------------------------------------------------------------------------- 
Claridad              Puede volverse largo    Más limpio con varios valores
                      con muchos casos 

---->Situaciones útiles 
1.Menús de opciones 
2.Respuestas según tipo de dato o valor exacto 
3.Procesar distintos comandos o entradas del usuario 

EJEMPLO: 

opcion = int(input("Ingresa una opción (1-3): "))

match opcion:
    case 1:
        print("Has elegido ver el catálogo.")
    case 2:
        print("Has elegido realizar una compra.")
    case 3:
        print("Has elegido salir del sistema.")
    case _:
        print("Opción inválida. Intenta nuevamente.") 