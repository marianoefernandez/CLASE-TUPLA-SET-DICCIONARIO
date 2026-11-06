# Pantalla
VENTANA = (1920, 1080)          # (ancho, alto)
COLOR_FONDO = (255, 0, 0)             # (R, G, B)
# Servidor
SERVIDOR = ("localhost", 8080)         # (host, puerto)
# Base de datos
CONEXION_DB = ("127.0.0.1", 5432, "admin", "sistema_db")  # (host, puerto, usuario, base)
# Rangos
RANGO_EDAD = (18, 99)                  # (mínimo, máximo)
MENSAJE_ERROR_EDAD = ("Error, la edad no puede estar vacia ","Error, la edad es invalida: ","Error, la edad esta fuera del rango permitido (18 a 99) ")

RANGO_DNI = (1000000,99999999)
MENSAJE_ERROR_DNI = ("Error, el dni no puede estar vacio ","Error, el dni es invalida: ","Error, el dni esta fuera del rango permitido (7 a 8 digitos) ")

RANGO_NOTA = (1,10)
MENSAJE_ERROR_NOTA = ("Error, la nota no puede estar vacia ","Error, la nota es invalida: ","Error, la nota esta fuera del rango permitido (1 a 10) ")


HORARIO_ATENCION = (9, 18)             # (apertura, cierre)
# Opciones válidas
IDIOMAS_SOPORTADOS = ("es", "en", "pt")
# Versión
VERSION = (2, 4, 1)                    # (mayor, menor, parche)

ASC = True
DESC = False