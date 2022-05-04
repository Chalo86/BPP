"""
Descripción
-----------
Este módulo define las funciones necesarias para la solución de la asignación #2 de BPP

Las funciones creadas son:

- :func:`create_df`
- :func:`check`
- :func:`tarea`

Librerías y módulos
-------------------
- ``pandas`` librería requerida para la creación y gestión de DataFrames
- ``plotly`` necesario para la creación de las gráficas
- ``os`` para la creación del directorio donde se almacenará la gráfica
- :mod:`errors` excepciones especialmente definidas para la aplicación

"""

import pandas as pd
from errors import EmptyError,ColumnError,SepsError
import plotly.express as px
import os

def create_df(path, columns, seps=[',',]):
    """Función responsable de importar el archivo *csv*, su validación y creación del DataFrame

    Asimismo, la función será capaz de generar distintas excepciones en caso de error

    La función :func:`create_df` validará:

    - Que el DataFrame generado posea la misma cantidad de columnas que el *csv* suministrado
    - Que las columnas del DataFrame sean las indicadas por el usuario
    - Que no existan columnas vacías en el DataFrame

    :param path: Representa el ``path`` donde se encuentra el fichero *csv*
    :type path: str
    :param columns: Representa la ``lista`` de columnas esperadas en el DataFrame
    :type columns: list
    :param seps: Representa una ``lista`` de posibles separadores para el DataFrame, defaults to [ ' , ' , ]
    :type seps: list, optional
    :raises SepsError: Excepción generada en caso de no suministrar el separador correcto
    :raises ColumnError: Excepción generada en caso de no suministrar las columnas correctas
    :raises EmptyError: Excepción generada en caso de obtener una o varias columnas vacías
    :raises AssertionError: Excepción generada en caso de no suminitrar el tipo de dato correcto de los argumentos
    :return: El DataFrame generado del fichero *csv*
    :rtype: pd.DataFrame
    """

    #Validación de los argumentos
    assert(type(path)==str),f'Argumento "path" debe ser un string y fue suministrado un {type(path)}'
    assert(type(columns)==list),f'Argumento "columns" debe ser de tipo lista y fue suministrado un {type(columns)}'
    assert(type(seps)==list),f'Argumento "seps" debe ser de tipo lista y fue suministrado un {type(seps)}'
    assert(all(isinstance(x,str) for x in seps)),'Elementos en seps deben ser del tipo string'

    df = pd.read_csv(path,sep=seps[0]) #Creación del DataFrame
    check = False

    # Primera validación: Validación del constructor y pruebas con separadores
    if len(df.columns) == len(columns):
        check = True 
    else:
        for item in seps[1:]:
            df = pd.read_csv(path,sep=item)
            if len(df.columns)==len(columns):
                check = True
                break

    # Segunda validación: Columnas en el DataFrame y separador
    if not check:
        if len(df.columns)==1:
            raise SepsError
        raise ColumnError('El Dataframe no posee la cantidad de columnas indicadas')
    
    for col in columns:
        if col not in df.columns:
            raise ColumnError(f'Columna {col} no se encuentra en el DataFrame')
    
    cols_vals = {col:df[col].isna().values.all() for col in df.columns}
    
    # Tercera validación: Datos en las columnas
    if sum(cols_vals.values()) != 0:
        raise EmptyError('Validar DataFrame y/o separadores suministrados\n'+'Columnas vacias\n' + f'{cols_vals}')

    return df

def check(col):
    """Función de soporte que nos permitirá validar los datos incluidos en el DataFrame
    
    .. note:: 
        La función :func:`check` ha sido diseñada para ser aplicada a través del método ``apply``
        de la librería ``pandas``

    Pasos que ejecuta la función:

    - Se validará que los elementos del DataFrame sean númericos 
    - Se eliminarán las comillas simples y/o dobles de las celdas donde existan
    - Se convertirán los errores y/o **NaN** en `0`

    :param col: Columna del DataFrame donde se realizará la verificación de los elementos
    :type col: pd.Series
    :return: La columna cuyos elementos han sido validados y convertidos a un dtype numérico
    :rtype: pd.Series
    """
    if col.dtypes == 'O':
        col = col.str.replace("'",'')
        col = col.str.replace('"','')
        col = pd.to_numeric(col,errors='coerce').fillna(0)
    return col

# Función para resolver la parte 1 de la asignación:
def tarea(df):
    """Función diseñada para la evaluación del DataFrame suministrado con el objetivo 
    responder las preguntas correspondientes a la asignación #1 de BPP

    .. note:: 
        Esta función no generará el return de una variable, sólo realiza la evaluación de las
        pregurntas e imprime en pantalla las respuestas correspondientes. A su vez, se generará
        un directorio ``Imagenes`` en el path del script con la gráfica requerida 
    
    Preguntas de la asigncación #2:

    1. ¿Qué mes se ha gastado más?
    2. ¿Qué mes se ha ahorrado más?
    3. ¿Cuál es la media de gastos del año?
    4. ¿Cuál ha sido el gasto total a lo largo del año?
    5. ¿Cuáles han sido los ingresos totales a lo largo del año?
    6. Gráfica de los ingresos a lo largo del año

    :param df: DataFrame que será analizado para responder a la asignación
    :type df: pd.DataFrame
    """
    df.loc['Gasto'] = df[df<0].sum()
    """Nueva fila incluida en el DataFrame `Gasto` representa la suma de los valores < 0"""
    df.loc['Ahorro'] = df[df>0].sum()
    """Nueva fila incluida en el DataFrame `Ahorro` representa la suma de los valores > 0"""
    # Ahora tenemos toda la información ordenada para proceder a responder las preguntas del apratado 1 de la asignación:

    # 1. ¿Qué mes se ha gastado más?
    mes_gasto = df[df == df.loc['Gasto'].max()].loc['Gasto'].idxmax()
    print('¿Qué mes se ha gastado más?\n'+
        f'{mes_gasto}')

    # 2. ¿Qué mes se ha ahorrado más?
    mes_ahorro = df[df == df.loc['Ahorro'].max()].loc['Ahorro'].idxmax()
    print('¿Qué mes se ha ahorrado más?\n'+
        f'{mes_ahorro}')

    # 3. ¿Cuál es la media de gastos al año?
    gasto_mean = '{:+,.2f}'.format(df.loc['Gasto'].mean())
    print('¿Cuál es la media de gastos al año?\n'+
        f'{gasto_mean}')

    # 4. ¿Cuál ha sido el gasto total a lo largo del año?
    gasto_total = '{:+,.2f}'.format(df.loc['Gasto'].sum())
    print('¿Cuál ha sido el gasto total a lo largo del año?\n'+
        f'{gasto_total}')

    # 5. ¿Cuáles han sido los ingresos totales a lo largo del año?
    ingreso_total = '{:,.2f}'.format(df.loc['Ahorro'].sum())
    print('¿Cuáles han sido los ingresos totales a lo largo del año?\n'+
        f'{ingreso_total}')

    # 6. Gráfica de los ingresos a lo largo del año
    # Separo la data de Gastos y Ahorro por mes en un DataFrame independiente data2
    data2 = df.loc[['Ahorro','Gasto']]

    # Creamos la gráfica
    fig = px.bar(data2.transpose(),opacity=0.7,title='Gasto y Ahorro por mes',text_auto=True)
    fig.layout.xaxis.title.text = 'Mes'
    fig.layout.yaxis.title.text = 'Valor'

    # Vamos a pasar la gráfica a una imagen
    # Creamos un fichero Imagenes (en caso de que no exista)
    if not os.path.exists('Imagenes'):
        os.mkdir('Imagenes')

    #Creamos la imagen de la gráfica
    fig.write_image('Imagenes/fig1.png',width=1200, height=600, scale=2)
    dir = os.path.abspath('Imagenes/fig1.png')
    print('Gráfica de ingresos a lo largo del año\n'+
        f'Gráfica almacenada en {dir}')