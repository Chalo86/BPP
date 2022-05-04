"""
Descripción
-----------
Este módulo contiene la definición de un grupo específico de errores diseñados para la asignación #2 de BPP

En partícular se busca dar solución a la segunda parte de la asignación al generar 
Excepciones especificas para errores generados tras la creación de DataFrames provenientes de *csv*

Dichas Excepciones han sido diseñadas para trabajar en conjunto con el módulo :mod:`funciones`

"""

# Parte 1: Comprobación del archivo y tratamiento de la data
# Nota: Este apartado pertenece a la segunda parte de la asignación

# Debido a que me gusto lo aprendido en clases de crear nuestras propias excepciones, 
# decidí crear 3 especificas para el ejercicio propuesto con la intención de prácticar!!!
class Errors(Exception):
    """
    Un objeto :class:`Errors` hereda de la clase ``Exception`` todos sus atributos

    .. note:: 
        Las excepciones definidas que heredan de la clase **Exception** pueden ser 
        usadas como cualquier excepción de Python

    :param Exception: Clase del core de `Python` de la cual heredaremos sus atributos
    :type Exception: class
    """
    __module__ = ''

class ColumnError(Errors):
    """
    Un objeto :class:`ColumnError` hereda de la clase :class:`Errors` todos sus atributos

    ::

         ColumnError ha sido diseñado para ser usado durante la creación de un DataFrame
         El mismo será usado para señalar diferencias en las columnas obtenidas con las esperadas

    :param Exception: Clase del core de ``Python`` de la cual heredaremos sus atributos
    :type Exception: class
    """
    pass

class SepsError(Errors):
    """
    Un objeto :class:`SepsError` hereda de la clase :class:`Errors` todos sus atributos
    
    ::

         SepsError ha sido diseñado para ser usado durante la creación de un DataFrame
         El mismo será usado para señalar que el separación definido para el csv no es correcto

    :param Exception: Clase del core de ``Python`` de la cual heredaremos sus atributos
    :type Exception: class
    """
    pass

class EmptyError(Errors):
    """Un objeto :class:`EmptyError` hereda de la clase :class:`Errors` todos sus atributos
    
    ::

        EmptyError ha sido diseñado para ser usado durante la creación de un DataFrame
        El mismo será usado para señalar que existen columans vacías en el DataFrame creado

    :param Exception: Clase del core de ``Python`` de la cual heredaremos sus atributos
    :type Exception: class
    """
    pass