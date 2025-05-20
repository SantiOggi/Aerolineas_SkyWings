def menu()->None:
    """
    La función imprime el menú de opciones.\n
    No recibe argumentos ni retorna nada.
    """
    print(
        """
        ------------------------------------------------
                         MENÚ PRINCIPAL
                Elija el número de opción deseado
        ------------------------------------------------
        1- Cargar vuelos.
        2- Buscar vuelo por código.
        3- Mostrar vuelo más caro.
        4- Mostrar vuelo más barato.
        5- Mostrar vuelos con precio mayot a $100.000.
        6- Mostrar matriz de vuelos. 
        7- Salir del programa.
        ------------------------------------------------
        """)

def opcion_valida()->int:
    """
    La función se asegura de que el valor elegido esté dentro
    de los valores permitidos.

        Return: Número de opción elegida.
    """
    flag = False
    while not flag:
        opcion = input("Ingrese el número de opción: ")
        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= 7:
                flag = True
            else:
                print("El número está fuera del rango de opciones.")
        else:
            print("No ingresaste un número.")
    return opcion

def cantidad_vuelos()-> int:
    """
    La función pregunta la cantidad de vuelos a cargar, \n
    y verifica que se ingrese un número.

        Return: devuelve el número verificado.
    """
    flag = False
    while not flag:
        cantidad = input("Ingrese la cantidad de vuelos que quiere cargar(maximo 10): ")
        if cantidad.isdigit():
            cantidad = int(cantidad)
            if 1 <= cantidad <= 10:
                flag = True
            else:
                print("No se pueden cargar más de 10 vuelos por vez.")
        else:
            print("No ingresaste un número.")
    return cantidad    

def cargar_vuelos(matriz: list, cantidad: int)-> None:
    """
    La función ubica el primer espacio libre de la matriz, \n
    y pide los datos de los vuelos a ingresar, para agregarlos a la matriz original.

        Args:
            matriz: es la matriz de vuelos.
            cantidad: cantidad de vuelos que se van a cargar.
    """
    for i in range(len(matriz)):
        if matriz[i] == [None]:
            posicion_libre = i
            break
    
    for j in range(cantidad):
        vuelo = validacion_vuelo()
        destino = input("Ingrese el país de destino: ")
        precio = int(input("Ingrese el precio del pasaje: "))
        matriz[posicion_libre+j] = [vuelo, destino, precio]

def validacion_vuelo()->str:
    """
    La función valida que el número de vuelo cargado cumpla con las condiciones pedidas.

        Return: devuelve el codigo de vuelo.
    """
    flag = False
    while not flag:
        largo = False
        digitos = False
        vuelo = input("Ingrese el número de vuelo: ")
        if len(vuelo) < 5:
            print("El número de vuelo debe tener al menos 5 dígitos. Ingreselo nuevamente.")
        else:
            largo = True

        if vuelo.isdigit():
            digitos = True
        else:
            print("El número de vuelo debe tener sólo digitos numéricos.")
        
        if largo and digitos:
            flag = True
    return vuelo

def buscar_por_codigo(matriz: list)-> None:
    """
    La función pide un número de vuelo y lo compara con los cargados en la matriz recibida.
    Si encuentra coincidencias las imprime, si no lo informa.
    """
    vuelo = validacion_vuelo()
    flag = False
    for i in range(len(matriz)):
        if matriz[i][0] == vuelo:
            print(matriz[i])
            flag = True

    if not flag:
        print("No hay ningún vuelo con el código ingresado.")

def mostrar_mas_caro(matriz: list)-> None:
    """
    La función busca el precio más alto en la lista 
    e imprime todos los vuelos que lo igualen.
    """
    precio_max = 0
    for i in range(len(matriz)):
        if matriz[i][2] > precio_max:
            precio_max = matriz[i][2]

    for j in range(len(matriz)):
        if matriz[j][2] == precio_max:
            print(matriz[j])
    
    if precio_max == 0:
        print("No se cargaron vuelos aún.")

def mostrar_mas_barato(matriz: list)-> None:
    """
    La función busca el precio más bajo en la lista 
    e imprime todos los vuelos que lo igualen.
    """
    precio_min = 100000000000000000000
    for i in range(len(matriz)):
        if matriz[i][2] < precio_min:
            precio_min = matriz[i][2]

    for j in range(len(matriz)):
        if matriz[j][2] == precio_min:
            print(matriz[j])
    
    if precio_min == 100000000000000000000:
        print("No se cargaron vuelos aún.")
          
def mostrar_mayores_a_100mil(matriz: list)-> None:
    flag = False
    for i in range(len(matriz)):
        if matriz[i][2] > 100000:
            print(matriz[i])
            flag = True
    if not flag:
        print("No hay vuelos cargados que cuesten más de $100.000")
    
def mostrar_matriz(matriz: list)-> None:
    """
    La función muestra por consola la matriz, evitando los espacios vacíos.
    """
    for i in range(len(matriz)):
        if matriz[i] != [None]:
            print(matriz[i])