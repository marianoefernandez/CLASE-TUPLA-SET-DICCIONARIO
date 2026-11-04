def reemplazar_caracteres(cadena_original:str,caracter_reemplazar:str,reemplazo:str) -> str:
    """Reemplaza cada aparición exacta de un texto por otro.

    Args:
        cadena_original: Cadena en la que se buscarán coincidencias.
        caracter_reemplazar: Texto que se desea reemplazar.
        reemplazo: Texto que ocupará el lugar de cada coincidencia.

    Returns:
        Una nueva cadena con los reemplazos aplicados.
    """
    cadena_copia = ""
    
    for i in range(len(cadena_original)):
        if cadena_original[i] == caracter_reemplazar:
            cadena_copia += reemplazo
        else:
            cadena_copia += cadena_original[i]

    return cadena_copia

def verificar_es_entero(cadena:str) -> bool:
    """Comprueba que una cadena represente un entero no negativo.

    Solo acepta cadenas no vacías formadas por dígitos decimales; no admite
    signos ni separadores.

    Args:
        cadena: Texto que se desea validar.

    Returns:
        `True` si todos sus caracteres son dígitos; de lo contrario, `False`.
    """
    if verificar_cadena(cadena):
        for i in range(len(cadena)):
            caracter_ascii = ord(cadena[i])
            if not verificar_numero(caracter_ascii):
                return False

        return True
    else:
        return False

def verificar_numero(caracter_ascii:int) -> bool:
    """Indica si un código ASCII corresponde a un dígito decimal.

    Args:
        caracter_ascii: Código entero del carácter que se desea comprobar.

    Returns:
        `True` para los códigos ASCII de `0` a `9`; de lo contrario, `False`.
    """
    return caracter_ascii >= 48 and caracter_ascii <= 57

def verificar_cadena(cadena:str) -> bool:
    """Comprueba que el valor sea una cadena no vacía.

    Args:
        cadena: Valor que se desea validar.

    Returns:
        `True` si el tipo exacto es `str` y contiene al menos un carácter;
        de lo contrario, `False`.
    """
    return type(cadena) == str and len(cadena) > 0
