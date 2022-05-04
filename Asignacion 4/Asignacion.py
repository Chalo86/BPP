from pickprimes import is_prime
import pdb

print('Bienvenido a la Asignación #4 de BPP \n')
# --------------------- Actividad #1 -----------------------
def actividad_1():
    print('==================================================================================')
    print('Actividad #1: encontrar el máximo elemento de cada lista dentro de una lista\n')

    try:
        n = int(input('Por favor indicar cuantas listas se encuentran dentro de la lista: '))

    except ValueError as e:
        print('\n-----------------------------------------------------------------')
        print('ERROR:')
        msg = 'La cantidad de listas debe ser un número entero\n'
        print(msg,e)
        print('-----------------------------------------------------------------')
        print('\nPasaremos a la siguiente actividad')
        return False, msg

    else:
        print('\n----------------------------------------------------------------')
        print('Nota: se debe separar los elelmentos de cada lista con espacio')
        print('----------------------------------------------------------------\n')

        try:
            test_case = [list(map(int,input(f'Ingrese los elementos de la lista #{i}: ').split())) for i in range(1,n+1)]

        except ValueError as e:
            print('\n-----------------------------------------------------------------')
            print('ERROR:')
            msg = 'Los valores indicados de cada lista deben ser enteros\n'
            print(msg,e)
            print('-----------------------------------------------------------------')
            print('\nPasaremos a la siguiente actividad')
            return False, msg

        else:
            # Creación del resultado de la Actividad #1
            pdb.set_trace()
            return [max(lista) for lista in test_case], None

# --------------------- Actividad #2 -----------------------
def actividad_2():
    print('\n==================================================================================')
    print('Actividad #2: encontrar los números primos en la lista suministrada')

    print('\n----------------------------------------------------------------')
    print('Nota: se debe separar los elementos de la lista con espacio')
    print('----------------------------------------------------------------\n')

    try:
        test_case_2 = list(map(int,input(f'ingrese los elementos de la lista: ').split()))

    except ValueError as e:
        print('\n-----------------------------------------------------------------')
        print('ERROR:')
        msg = 'Los valores de cada elemento en la lista deben ser enteros\n'
        print(msg,e)
        print('-----------------------------------------------------------------')
        print('\nGeneramos el resumen')
        return False, msg

    else: 
        # Creación del resultado de la Actividad #2
        return list(filter(is_prime, test_case_2)), None

# --------------------- Loop de validación -----------------------
def ask():
    while True:
        try:
            next = input('\n¿Desea volver a intentar la(s) actividad(es) con error (y,n)? [y]: ')
            
            if next == '':
                next = 'y'
            
            if next not in ('y','n'):
                raise ValueError
        
        except ValueError:
            print(f'Por favor seguir las instrucciones de pantalla')
            print(f'Únicas opciones posibles [y , n]: "{next}" no es valida\n')
        
        else:
            return next

# --------------------- Main -----------------------
result, msg1 = actividad_1()
primes, msg2 = actividad_2()

while True:
    print('\n==================================================================================')
    print('RESUMEN:')

    if not result and not primes:
        print('\nPor favor seguir las instrucciones en pantalla para lograr obtener los resultados')
        print(f'\nError identificado en la Actividad #1: \n{msg1}')
        print(f'\nError identificado en la Actividad #2: \n{msg2}')
        
        seguir = ask()
        
        if seguir == 'n':
            break
        
        else:
            result, msg1 = actividad_1()
            primes, msg2 = actividad_2()

    elif not result:
        print('\nError identificado durante la Actividad #1')
        print(f'{msg1}')
        print(f'\nResultado de la Actividad #2:')
        print(f'Los números primos encontrados son: \n{sorted(primes)}')

        seguir = ask()
        
        if seguir == 'n':
            break

        else:
            result, msg1 = actividad_1()
   
    elif not primes and msg2:
        print(f'\nResultado de la Actividad #1:')
        print(f'El mayor elemento de cada sub-lista es: \n{result}')
        print('\nError identificado durante la Actividad #2')
        print(f'{msg2}')

        seguir = ask()
        
        if seguir == 'n':
            break

        else:
            primes, msg2 = actividad_2()

    else:
        print(f'\nResultado de la Actividad #1:')
        print(f'El mayor elemento de cada sub-lista es: \n{result}')
        print(f'\nResultado de la Actividad #2:')
        print(f'Los números primos encontrados son: \n{sorted(primes)}')
        print('\nGracias por usar la Aplicación!!!!!!\n')
        break