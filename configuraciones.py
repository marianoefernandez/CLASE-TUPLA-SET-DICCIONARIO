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

HORARIO_ATENCION = (9, 18)             # (apertura, cierre)
# Opciones válidas
IDIOMAS_SOPORTADOS = ("es", "en", "pt")
# Versión
VERSION = (2, 4, 1)                    # (mayor, menor, parche)