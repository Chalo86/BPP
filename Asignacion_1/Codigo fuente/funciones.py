import pandas as pd
from errors import EmptyError,ColumnError,SepsError
import plotly.express as px
import os

# Creamos una función responsable de importar el csv y su validación, en caso de error se genera una excepción
# 1. Se comprueba el fichero y cantidad de columnas
# 2. se comprueba que las columnas sean las indicadas por el usuario
# 3. Se valida que no existan columnas vacias

def create_df(path, columns, seps=[',',]):
    """Crea un dataframe de un archivo csv despúes de validar las columnas
    path:str -> path donde se encuentra ubicado el csv
    columns:list -> lista con las columnas en el csv
    sep:list -> lista con los posibles separadores usados en el csv """
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

# Procedemos a crear una función que nos ayude a validar los daros del Dataframe.
# Pasos de la función:
# - Al trabajar con data numérica se validará solo columnas que no posean valores numéricos
# - Se eliminaran las comillas simples o dobles de las celdas que contengan comillas
# - Se convertirán los errores y/o NaN en 0 
# La función se aplicará al Dataframe a través del método apply()

def check(col):
    if col.dtypes == 'O':
        col = col.str.replace("'",'')
        col = col.str.replace('"','')
        col = pd.to_numeric(col,errors='coerce').fillna(0)
    return col

# Función para resolver la parte 1 de la asignación:
def tarea(df):
    # Para poder continuar con el análisis, procederemos a incluir dos nuevas filas al DataFrame.
    # - 'Ahorro': será la suma de todos los valores >0 de cada mes
    # - 'Gasto': será la suma de todos los valores <0 de cada mes
    df.loc['Gasto'] = df[df<0].sum()
    df.loc['Ahorro'] = df[df>0].sum()

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