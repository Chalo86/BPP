# Parte 1: Comprobación del archivo y tratamiento de la data
# Nota: Este apartado pertenece a la segunda parte de la asignación

# Debido a que me gusto lo aprendido en clases de crear nuestras propias excepciones, 
# decidí crear 3 especificas para el ejercicio propuesto con la intención de prácticar!!!
class Errors(Exception):
    pass

class ColumnError(Errors):
    pass

class SepsError(Errors):
    pass

class EmptyError(Errors):
    pass
