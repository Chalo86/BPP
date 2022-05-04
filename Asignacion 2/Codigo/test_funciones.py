from funciones import create_df, check
import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from errors import EmptyError,ColumnError,SepsError

class TestAsignacionFunc(unittest.TestCase):
    def setUp(self):
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
            self.df2_func = df2_func
            self.df1 = df1
            self.df2 = df2           

    def test_func_create_df(self):
        '''Pureba para validar que la función crea un dataframe correctamente'''
        # assert_frame_equal solo compara items del mismo tipo dentro de cada columna
        # por ello se debe hacer uso de dos dataframes identicos.
        assert_frame_equal(self.df2_func,self.df2)

    def test_func_check(self):
        'Comprobación de la func check para transformar columnas del dataframe'
        assert_frame_equal(self.df1_func,self.df1)

    def test_df_qty_columns(self):
        '''Validación de la cantidad de columnas de los dataframes'''
        self.assertEqual(len(self.df1_func.columns),len(self.df1.columns))
        self.assertEqual(len(self.df2_func.columns),len(self.df2.columns))

    def test_df_columns(self):
        '''Validación de que todas las columnas requeridas esten incluidas'''
        for col in self.df1_func.columns:
            self.assertIn(col,self.columns)
    
    def test_df_columns_not_empty(self):
        '''Validación de que todas las columnas del dataFrame no estan vacias'''
        for col in self.df1_func.columns:
            self.assertNotEqual(self.df1_func[col].sum(),0)

    def test_input_column(self):
        '''Comprobación de los inputs de entrada: Faltan columnas por indicar'''
        with self.assertRaises(ColumnError):
            columns = ['a','b','c']
            create_df(self.path1,columns,self.sep)
    
    def test_input_column2(self):
        '''Comprobación de los inputs de entrada: Columnas de más indicadas'''
        with self.assertRaises(ColumnError):
            columns = ['a','b','c','d',9]
            create_df(self.path1,columns,self.sep)
    
    def test_input_sep(self):
        '''Comprobación de los inputs de entrada: Separador incorrecto'''
        with self.assertRaises(SepsError):
            sep = [',']
            create_df(self.path1,self.columns,sep)
    
    def test_input_empty_column(self):
        '''Comprobación de los inputs de entrada: Columna vacia'''
        with self.assertRaises(EmptyError):
            path = 'prueba3.csv'
            create_df(path,self.columns,self.sep)

# Para comprobar que la función responda correctamente a argumentos erroneos por 
# parte del usuario haré uso del decorador "expectedFailure"
class ExpectedFailureTest(unittest.TestCase):
    def setUp(self):
        self.path = 'prueba.csv'
        self.columns = ['a','b','c','d']
        self.sep = [';']
    
    @unittest.expectedFailure
    def test_fail_path(self):
        '''Comprobación de error por el tipo del argumento "path"'''
        path = 2
        create_df(path,self.columns,self.sep)
       
    @unittest.expectedFailure
    def test_fail_path2(self):
        '''Comprobación de error por el tipo del argumento "path"'''
        path = [2]
        create_df(path,self.columns,self.sep)
       
    @unittest.expectedFailure
    def test_fail_column(self):
        '''Comprobación de error por el tipo del argumento "columns"'''
        columns = 2
        create_df(self.path,columns,self.sep)
    
    @unittest.expectedFailure
    def test_fail_column2(self):
        '''Comprobación de error por el tipo del argumento "columns"'''
        columns = '2'
        create_df(self.path,columns,self.sep)
    
    @unittest.expectedFailure
    def test_fail_sep(self):
        '''Comprobación de error por el tipo del argumento seps'''
        sep = (';',)
        create_df(self.path,self.columns,sep)
    
    @unittest.expectedFailure
    def test_fail_sep2(self):
        '''Comprobación de error por el tipo del argumento seps'''
        sep = 8.0
        create_df(self.path,self.columns,sep)
    
    @unittest.expectedFailure
    def test_fail_sep3(self):
        '''Comprobación de error por el tipo de los elementos del argumento seps'''
        sep = [';',3]
        create_df(self.path,self.columns,sep)
    
if __name__ == '__main__':
    unittest.main()