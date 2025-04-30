import os
import pandas as pd
from utils import (
    preparar_dataframe, producto_top, ingresos_totales_por_producto,
    mostrar_ingreso_total, grafico_ventas_diarias,
    resumen_diario_detallado
)


# Ruta segura relativa al script, esto lo hice porque no me queria leer el cvs y investigue que agregando esta ruta relativa me solucionaba el problema
'''
os.path.abspath(__file__) == Convierte la ruta de __file__ en una ruta absoluta, aunque ejecute el archivo desde otra carpeta me dice exactamente donde esta ubicado.
os.path.dirname == ruta absoluta a la carpeta donde está el script main 
os.path.join == Une la ruta con el nombre del archivo csv
Esto me ayudo a solucionar el problema que tenia con FileNotFoundError: 'ventas_marzo.csv'
'''
base_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_path, "ventas_marzo.csv")

# Leer el archivo CSV desde la ruta correcta
df = pd.read_csv(file_path)
df = preparar_dataframe(df)

# Menú 
def mostrar_menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1 - Ver resumen general de ventas por día y producto")
        print("2 - Producto más vendido del mes")
        print("3 - Ingreso total por producto")
        print("4 - Ingreso total general del mes")
        print("5 - Ver gráfico de ventas diarias")
        print("0 - Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            resumen_diario_detallado(df)
        elif opcion == "2":
            producto_top(df)
        elif opcion == "3":
            ingresos_totales_por_producto(df)
        elif opcion == "4":
            mostrar_ingreso_total(df)
        elif opcion == "5":
            grafico_ventas_diarias(df)
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

mostrar_menu()
