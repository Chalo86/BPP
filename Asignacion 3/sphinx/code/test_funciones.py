"""
Descripción
-----------
Este es el sript principal de la asignación, en el se definen las pruebas unitarias diseñadas para el test.

Las pruebas creadas son:

- :func:`TestAsignacionFunc.test_func_create_df`
- :func:`TestAsignacionFunc.test_func_check`
- :func:`TestAsignacionFunc.test_df_qty_columns`
- :func:`TestAsignacionFunc.test_df_columns`
- :func:`TestAsignacionFunc.test_df_columns_not_empty`
- :func:`TestAsignacionFunc.test_input_column`
- :func:`TestAsignacionFunc.test_input_column2`
- :func:`TestAsignacionFunc.test_input_sep`
- :func:`TestAsignacionFunc.test_input_empty_column`
- :func:`ExpectedFailureTest.test_fail_path`
- :func:`ExpectedFailureTest.test_fail_path2`
- :func:`ExpectedFailureTest.test_fail_column`
- :func:`ExpectedFailureTest.test_fail_column2`
- :func:`ExpectedFailureTest.test_fail_sep`
- :func:`ExpectedFailureTest.test_fail_sep2`
- :func:`ExpectedFailureTest.test_fail_sep3`

.. note:: 
    Es necesario disponer de los siguientes ficheros csv para poder realizar las pruebas. 
    Asimismo, deben encontrase en el mismo directorio donde se almacene los archivos ``.py``

    1. *prueba.csv*
    2. *prueba2.csv*
    3. *prueba3.csv*

Librerías y módulos
-------------------
- ``unittest`` librería utilizada para para el desarrollo de las pruebas
- ``pandas`` librería requerida para la creación y gestión de DataFrames
- ``assert_fram_equal`` método de ``pandas.testing`` requerido para evaluar si DataFrames son iguales
- :mod:`errors`: Excepciones especialmente definidas para la aplicación
- :mod:`funciones`: contiene las funciones que vamos a probar ``create_df`` y ``check``

"""

from funciones import create_df, check
import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from errors import EmptyError,ColumnError,SepsError

class TestAsignacionFunc(unittest.TestCase):
    """
    Clase que contiene todos los test unitarios donde se espera una respuesta positiva luego de la evaluación

    La clase :class:`TestAsignacionFunc` hereda sus atributos de la clase ``TestCase`` del paquete ``unittest``
    
    :param unittest.TestCase: Clase del paquete ``unittest`` de la cual heredaremos sus atributos
    :type unittest.TestCase: class
    """
    def setUp(self):
        """
        :func:`setUp` es un método reservado de la clase ``TestCase`` que permite definir un contructor para los
        casos de prueba. 
        
        Este método se ejecutará antes que las pruebas para asegurar que las variables esten 
        disponibles para las pruebas, evitando la repetición de la creación de dichas variables en cada prueba
       
        .. note:: 
            Recordar que se debe disponer de los ficheros *csv* en el directorio del proyecto
            En caso de no tenerlos la prueba se cancelará haciendo uso del método ``skipTest()`` 

            De igual forma es igual de importante poseer los ficheros originales ya que las pruebas 
            consisten en validar la igualdad de los DataFarmes generados
        
        **DataFrames de control**

        .. code-block:: python

            df1 = pd.DataFrame([[1,2,3,4],
                                [6,5,4,5],
                                [5,6,7,9],
                                [0,0,0,0]],
                                columns= ['a','b','c','d'],
                                dtype='float64')
        
        
        .. code-block:: python
        
            df2 = pd.DataFrame([[1,2,3,4],
                                [6,5,4,5],
                                [5,6,7,9]],
                                columns= ['a','b','c','d'])
        
        """
        self.path1 = 'prueba.csv'
        self.path2 = 'prueba2.csv'
        self.columns = ['a','b','c','d']
        self.sep = [';']
        try:
            df1_func = create_df(self.path1,self.columns,self.sep)
            df2_func = create_df(self.path2,self.columns,self.sep)
            df1_func = df1_func.apply(check)
            df1 = pd.DataFrame([[1,2,3,4],
                                [6,5,4,5],
                                [5,6,7,9],
                                [0,0,0,0]],
                                columns= ['a','b','c','d'],
                                dtype='float64')
            df2 = pd.DataFrame([[1,2,3,4],
                                [6,5,4,5],
                                [5,6,7,9]],
                                columns= ['a','b','c','d'])
        except IOError as e:
            print(e)
            self.skipTest(e)
        else:
            self.df1_func = df1_func
            """Variable de instancia perteneciente al DataFrame #1 creado por la función a probar
            DataFrame asociado al fichero `prueba.csv`"""
            self.df2_func = df2_func
            """Variable de instancia perteneciente al DataFrame #2 creado por la función a probar
            DataFrame asociado al fichero `prueba2.csv`"""
            self.df1 = df1
            """Variable de instancia perteneciente al DataFrame de control #1 
            DataFrame creado a través de `pandas`"""
            self.df2 = df2 
            """Variable de instancia perteneciente al DataFrame de control #2
            DataFrame creado a través de `pandas`"""          

    def test_func_create_df(self):
        '''Pureba para validar que la función :func:`funciones.create_df` crea un DataFrame correctamente'''
        # assert_frame_equal solo compara items del mismo tipo dentro de cada columna
        # por ello se debe hacer uso de dos dataframes identicos.
        assert_frame_equal(self.df2_func,self.df2)

    def test_func_check(self):
        '''Comprobación de la función :func:`funciones.check` para transformar columnas del DataFrame a tipo numérico'''
        assert_frame_equal(self.df1_func,self.df1)

    def test_df_qty_columns(self):
        '''Validación de la cantidad de columnas en ambos DataFrames creados por la función :func:`funciones.create_df`'''
        self.assertEqual(len(self.df1_func.columns),len(self.df1.columns))
        self.assertEqual(len(self.df2_func.columns),len(self.df2.columns))

    def test_df_columns(self):
        '''Validación de que todas las columnas requeridas esten incluidas en el DataFrame #1 creado'''
        for col in self.df1_func.columns:
            self.assertIn(col,self.columns)
    
    def test_df_columns_not_empty(self):
        '''Validación de que las columnas del DataFrame #1 creado no estan vacías'''
        for col in self.df1_func.columns:
            self.assertNotEqual(self.df1_func[col].sum(),0)

    def test_input_column(self):
        '''Comprobación de la función :func:`funciones.create_df` para inputs de entrada: Faltan columnas por indicar
        
        >>> columns = ['a','b','c']
        '''
        with self.assertRaises(ColumnError):
            columns = ['a','b','c']
            create_df(self.path1,columns,self.sep)
    
    def test_input_column2(self):
        '''Comprobación de la función :func:`funciones.create_df` para inputs de entrada: Columnas de más indicadas
        
        >>> columns = ['a','b','c','d',9]
        '''
        with self.assertRaises(ColumnError):
            columns = ['a','b','c','d',9]
            create_df(self.path1,columns,self.sep)
    
    def test_input_sep(self):
        '''Comprobación de la función :func:`funciones.create_df` para inputs de entrada: Separador incorrecto
        
        >>> sep = [',']
        '''
        with self.assertRaises(SepsError):
            sep = [',']
            create_df(self.path1,self.columns,sep)
    
    def test_input_empty_column(self):
        '''Comprobación de la función :func:`funciones.create_df` para inputs de entrada: Columna vacia
        
        .. note::
            Esta prueba unitaria hace uso del fichero ``prueba3.csv`` para la creación del 
            DataFrame y su posterior prueba
        
        >>> path = 'prueba3.csv'
        '''
        with self.assertRaises(EmptyError):
            path = 'prueba3.csv'
            create_df(path,self.columns,self.sep)

# Para comprobar que la función responda correctamente a argumentos erroneos por 
# parte del usuario haré uso del decorador "expectedFailure"
class ExpectedFailureTest(unittest.TestCase):
    """Clase que contiene todos las pruebas unitarias donde se espera un fallo durante la evaluación

    La clase :class:`ExpectedFailureTest` hereda sus atributos de la clase ``TestCase`` del paquete ``unittest`` 

    .. note::
        Los métdos definidos dentro de esta clase van acompañados del decorador ``@unitttest.expectedFailure``

    :param unittest.TestCase: Clase del paquete `unittest` de la cual heredaremos sus atributos
    :type unittest.TestCase: class
    """
    def setUp(self):
        """
        :func:`setUp` es un método reservado de la clase ``TestCase`` que permite definir un contructor para los
        casos de prueba. 
        
        Este método se ejecutará antes que las pruebas para asegurar que las variables esten 
        disponibles para las pruebas, evitando la repetición de la creación de dichas variables en cada prueba

        Durante esta implementación se han definido los 3 argumentos principales para la función :func:`funciones.create_df`

        **Variables:**
        
        1. ``path``: Directorio donde se encuentra el fichero *csv* a utilizar -> ``'prueba.csv'``
        2. ``columns``: Lista con las columnas definidas para la pureba -> ``['a','b','c','d']``
        3. ``seps``: Separador requerido para la correcta creación del DataFrame -> ``[';']``
        """
        self.path = 'prueba.csv'
        self.columns = ['a','b','c','d']
        self.sep = [';']
    
    @unittest.expectedFailure
    def test_fail_path(self):
        '''Comprobación de error por el tipo del argumento de ``path``
        
        Definición errada del argumento `path` con un tipo ``int``

        >>> path = 2
        '''
        path = 2
        create_df(path,self.columns,self.sep)
       
    @unittest.expectedFailure
    def test_fail_path2(self):
        '''Comprobación de error por el tipo del argumento de ``path``
        
        Definición errada del argumento `path` con un tipo ``list``

        >>> path = [2]
        '''
        path = [2]
        create_df(path,self.columns,self.sep)
       
    @unittest.expectedFailure
    def test_fail_column(self):
        '''Comprobación de error por el tipo del argumento de ``columns``
        
        Definición errada del argumento `columns` con un tipo ``int``

        >>> columns = 2
        '''
        columns = 2
        create_df(self.path,columns,self.sep)
    
    @unittest.expectedFailure
    def test_fail_column2(self):
        '''Comprobación de error por el tipo del argumento de ``columns``
        
        Definición errada del argumento `columns` con un tipo ``str``

        >>> columns = "2"
        '''
        columns = '2'
        create_df(self.path,columns,self.sep)
    
    @unittest.expectedFailure
    def test_fail_sep(self):
        '''Comprobación de error por el tipo del argumento de ``seps``
        
        Definición errada del argumento ``sep`` con un tipo ``tuple``

        >>> seps = (';',)
        '''
        sep = (';',)
        create_df(self.path,self.columns,sep)
    
    @unittest.expectedFailure
    def test_fail_sep2(self):
        '''Comprobación de error por el tipo del argumento de ``seps``
        
        Definición errada del argumento ``sep`` con un tipo ``float``

        >>> seps = 8.0
        '''
        sep = 8.0
        create_df(self.path,self.columns,sep)
    
    @unittest.expectedFailure
    def test_fail_sep3(self):
        '''Comprobación de error por el tipo de los elementos del argumento ``seps``
        
        Definición errada de los elementos del argumento ``sep``: no son del tipo ``str``

        >>> sep = [';',3]
        '''
        sep = [';',3]
        create_df(self.path,self.columns,sep)

if __name__ == '__main__':
    unittest.main()