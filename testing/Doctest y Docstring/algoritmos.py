#Ejecución por consola
#python -m doctest algoritmos.py
#python -m doctest algoritmos.py -v

"""
DOCTEST dentro de un script
>>> recursivo = Recursivo()
>>> recursivo.factorial(5)
120

>>> recursivo.factorial(13)
6227020800
"""

def fibonacci(number):
    if number == 0: return 0
    elif number == 1: return 1
    else: return fibonacci(number-1) + fibonacci(number-2)


def palindromo(sentence):
    """
    #DOCTEST mediante DOCSTRING dentro de las funciones
    Retorna verdadero si el parametro es un palindromo
    en caso contrario retorna falso

    sentence -- String o entero

    >>> palindromo("anita lava la tina")
    True

    >>> palindromo("CodigoFacilito")
    False
    """

    sentence = str(sentence).lower().replace(" ", "")
    return sentence == sentence[::-1] #verifica que sean iguales las lecturas de izq a der


class Recursivo:
    def factorial(self, number):
        if number == 0: return 1
        else: return number * self.factorial(number - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    #en consola:
    #python algoritmos.py

    #pruebas de un archivo externo
    doctest.testfile("test1.txt")