from funciones import verificar_array,eliminar_repeticiones,ordenar_array_caracteres,contar_dato,crear_conjunto_lista,calcular_intercepcion_listas

def mostrar_array(array:list,titulo:str = "",dato:str = "",mensaje_error:str = "Error, el array esta vacio"):
    if verificar_array(array):
        print(f"{titulo}",end="")
        for i in range(len(array)):
            print(f"{dato} {i + 1}°: {array[i]}")
    else:
        print(mensaje_error)

def mostrar_nombres_sin_repetir(lista_nombres:list,titulo:str = "LISTA DE NOMBRES\n") -> None:
    lista_nombres = eliminar_repeticiones(lista_nombres)
    ordenar_array_caracteres(lista_nombres)
    mostrar_array(lista_nombres,titulo,"nombre","ERROR, los nombres estan vacios")

def mostrar_nombres_repetidos(lista_repetida:list):
    nombres_sin_repetir = eliminar_repeticiones(lista_repetida)
    ordenar_array_caracteres(nombres_sin_repetir)

    for i in range(len(nombres_sin_repetir)):
        cantidad_repeticiones = contar_dato(lista_repetida,nombres_sin_repetir[i])
        print(f"{nombres_sin_repetir[i]} : {cantidad_repeticiones}")

def mostrar_nombres_entre_listas(lista_uno:list,lista_dos:list)-> None:
    #A las listas convertirlas en conjuntos
    lista_resultado = calcular_intercepcion_listas(lista_uno,lista_dos)
    ordenar_array_caracteres(lista_resultado)
    mostrar_array(lista_resultado,"RESULTADO FINAL\n","nombre","Error, no hay ningun nombre")

#MOSTRAR INFO EN EL DICCIONARIo

#FORMA ESPECIFICA --> SOLO SE ADAPTA AL DICCIONARIO QUE YO CREE

def mostrar_diccionario_alumno(alumno:dict,mensaje_error:str = "ERROR. El alumno no se puede mostrar") -> None:
    #SOLO FUNCIONA PARA MOSTRAR UN DICCIONARIO DE TIPO ALUMNO (legajo, nombre, apellido, dni, nota_final, edad)
    #EL FORMATO LO ELIGEN USTEDES
    if type(alumno) == dict:
        print(f"LEGAJO : {alumno.get("legajo")}")
        print(f"NOMBRE COMPLETO : {alumno.get("nombre")} {alumno.get("apellido")}")
        print(f"EDAD : {alumno.get("edad")} años")
        #print(f"DNI : {alumno.get("dni","NO ENCONTRADO")}")
        print(f"NOTA FINAL : {alumno.get("nota_final")}/10")
    else:
        print(mensaje_error)


#FORMA GENERICA

def mostrar_diccionario(diccionario:dict,mensaje_error:str = "ERROR. El diccionario no se puede mostrar") -> None:
    if type(diccionario) == dict:
        for clave in diccionario:
            #Que las claves se muestren en un formato bonito
            #Por ejemplo
            #en vez de que diga nombre diga --> NOMBRE o Nombre
            #en vez de que diga nota_final --> NOTA FINAL o Nota Final
            print(f"{clave} : {diccionario.get(clave)}")
    else:
        print(mensaje_error)


#MOSTRAR LISTA DE DICCIONARIOS

#GENERICA --> Tarea para casa

def mostrar_lista_diccionarios(lista_diccionarios:list,titulo:str = "",mensaje_error:str = "Error, el array esta vacio") -> None:
    pass

#ESPECIFICA --> SOLO FUNCIONA PARA LOS ALUMNOS DEL EJERCICIO
#nombre --> str
#apellido --> str
#legajo --> int (NO SE CARGAN, se genere de forma random)
#edad --> int
#nota_final --> int 

def mostrar_lista_alumnos(lista_alumnos:list,titulo:str = "MOSTRANDO ALUMNOS\n",mensaje_error:str = "ERROR, hubo un problema al mostrar a los alumnos") -> None:
    if verificar_array(lista_alumnos):
        print(titulo)
        for i in range(len(lista_alumnos)):
            if type(lista_alumnos[i]) == dict:
                mostrar_diccionario_alumno(lista_alumnos[i])
                print("")
    else:
        print(mensaje_error)