import pandas as pd
import matplotlib.pyplot as plt
##Preparo el data frame esto me permite poder hacerlo independiente
def preparar_dataframe(df):
    df["Fecha de Venta"] = pd.to_datetime(df["Fecha de Venta"])
    if "Ingreso" not in df.columns:
        df["Ingreso"] = df["Precio"] * df["Kilos Vendidos"]
    return df



#Opcion 1
def resumen_diario_detallado(df):
    resumen = df.groupby(["Fecha de Venta", "Producto"]).agg({
        "Kilos Vendidos": "sum",
        "Ingreso": "sum"
    }).reset_index()

    print("\n📅 Resumen diario de ventas por producto:\n")
    for fecha in resumen["Fecha de Venta"].dt.date.unique():
        print(f"🗓️  {fecha}")
        productos = resumen[resumen["Fecha de Venta"].dt.date == fecha]
        for _, row in productos.iterrows():
            print(f"   - {row['Producto']:<25} {row['Kilos Vendidos']:>6.2f} kg   ₡{row['Ingreso']:>10,.2f}")
        print("-" * 50)

#Opcion 2
def producto_top(df):
    top = df.groupby("Producto")["Kilos Vendidos"].sum().sort_values(ascending=False)
    producto = top.index[0]
    kilos = top.iloc[0]
    print("\nProducto más vendido del mes:")
    print(f"- {producto} con {kilos:.2f} kilos vendidos.")
    

#Opcion 3
def ingresos_totales_por_producto(df):
    ingresos = df.groupby("Producto")["Ingreso"].sum().sort_values(ascending=False)
    print("\n🧾 Ingreso total por producto:\n")
    for producto, ingreso in ingresos.items():
        print(f"- {producto:25} → ₡{ingreso:,.2f}") #Logre poner el signo de colones solo poniendolo como string 
        

#Opcion 4
def mostrar_ingreso_total(df):
    total = df["Ingreso"].sum()
    print(f"\nIngreso total del mes: ₡{total:,.2f}")
    
    

#Opcion 5
def grafico_ventas_diarias(df):
    resumen_diario = df.groupby("Fecha de Venta")["Kilos Vendidos"].sum()
    plt.figure(figsize=(12, 6))
    resumen_diario.plot(marker='o')
    plt.title("Ventas Diarias (Kilos) - Marzo 2025")
    plt.xlabel("Fecha")
    plt.ylabel("Kilos Vendidos")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    

            
            



