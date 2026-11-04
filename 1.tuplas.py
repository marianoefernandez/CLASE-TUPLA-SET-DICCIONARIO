from entradas import ingresar_entero_rango
from configuraciones import *

# #RECORRER TUPLA
# for i in range(len(COLOR_FONDO)):
#     print(f"COLOR {i + 1}: {COLOR_FONDO[i]}")

#COLOR_FONDO.append(200)#NO EXISTE APPEND
#TAMAÑO_VENTANA[0] = 1000#Al ser inmutables una vez definidas no se pueden modificar

#DESEMPAQUETADO
host,puerto = SERVIDOR#CORRECTO
# host = SERVIDOR#No estoy desempaquetando, estoy copiando la tupla en otra tupla
# host,puerto,lalala = SERVIDOR#ERROR, no puedo desempaquetar más elementos de los que la tupla tiene

print(f"SERVIDOR ABIERTO --> https://{host}:{puerto}")
# rojo,verde,azul = COLOR_FONDO#CORRECTO
# # rojo,verde = COLOR_FONDO#TAMPOCO SE PUEDE DESEMPAQUETAR MENOS VALORES DE LOS QUE HAY EN LA TUPLA
# print(f"\033[38;2;{rojo};{verde};{azul}mHola mundo\033[0m")

#EN CONCLUSION --> LA TUPLA SE DESEMPAQUETA COMPLETA

edad_persona = ingresar_entero_rango(RANGO_EDAD,"Ingrese la edad: ",MENSAJE_ERROR_EDAD)