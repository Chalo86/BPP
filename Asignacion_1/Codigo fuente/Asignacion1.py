from funciones import create_df, check, tarea
from errors import EmptyError,ColumnError,SepsError

# Declaración de los siguientes parámetros:
# - Path del archivo
# - Columnas
# - Posibles separadores

path = 'finanzas2020[1].csv'

columns = ['Enero','Febrero','Marzo','Abril','Mayo','Junio',
   'Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']

seps = [',',';',':','\t']

# Solución

try:
    # Generamos el Dataframe del archivo Finanzas2020 con ayuda de la función create_df
    data = create_df(path,columns,seps)

    # Haremos uso de la función "check" definida en el apartado anterior.
    data = data.apply(check)

except IOError:
        print(f'Validar el path suministrado: {path}. Archivo no encontrado')
except SepsError:
    print(f'Validar los separadores indicados para el csv: {seps}')
except EmptyError as e:
    print(e)
except ColumnError as e:
    print(e)
except AssertionError as e:
    print(e)

else:
    # Ejecutaremos la función tarea para obtener los resultads del ejercicio
    tarea(data)
