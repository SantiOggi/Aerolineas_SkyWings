from funciones import (menu,
                        opcion_valida,
                        cantidad_vuelos,
                        cargar_vuelos,
                        buscar_por_codigo,
                        mostrar_mas_caro,
                        mostrar_mas_barato,
                        mostrar_mayores_a_100mil,
                        mostrar_matriz)

from vuelos import matriz_vuelos

opcion = 0
while opcion != 7:
    menu()
    opcion = opcion_valida()
    match opcion:
        case 1:
            cantidad = cantidad_vuelos()
            cargar_vuelos(matriz_vuelos,cantidad)
    
        case 2:
            buscar_por_codigo(matriz_vuelos)

        case 3:
            mostrar_mas_caro(matriz_vuelos)

        case 4:
            mostrar_mas_barato(matriz_vuelos)

        case 5:
            mostrar_mayores_a_100mil(matriz_vuelos)
        
        case 6:
            mostrar_matriz(matriz_vuelos)

        case 7:
            print("Gracias por usar SkyWings.\n"
            "Esperamos que vuelva a volar con nosotros pronto.")
            opcion = 7

print("Programa finalizado.")