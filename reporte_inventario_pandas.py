import pandas as pd

datos = {
    'Producto': ['Laptop', 'Mouse', 'Monitor', 'Teclado', 'Cámara'],
    'Precio': [800, 25, 150, 45, 120],
    'Cantidad': [5, 20, 10, 15, 8]
}

df=pd.DataFrame(datos)

#crea una columna llamada total_inventario q sea resultado de
# multiplicar el precio por la cantidad de cada producto

df['Total_Inventario']=df['Precio']*df['Cantidad']


#filtrar los datos, muestra solo los productos cuyo precio
#sea mayor a 100
df_precio_mayor=df[df['Precio']>100]

#calcula la suma total de la columna total de inventario y
#el promedio de la columna Precio

suma_total=df['Total_Inventario'].sum()
promedio_precio=df['Precio'].mean()

print(f"La suma total del inventario es: {suma_total}")
print(f"El promedio de los precios es: {promedio_precio }")



#con el mismo dataframe el q incluye total_inventario:
#ordena el dataframe en forma descendente segun la columna

df_odenamiento=df.sort_values(by='Total_Inventario', ascending=False)
print("---------ORDENAMIENTO POR TOTAL INVENTARIO-------------")
print(df_odenamiento)

#estamos creando otra columna llamada 'Gama' con .loc
df.loc[df['Precio']>200, 'Gama']='Alta'
df.loc[df['Precio']<=200, 'Gama']='Estándar'
print(df)

#cuanto dinero tenemos invertido en cada gama
resumen=df.groupby('Gama')['Total_Inventario'].sum()
print("\n------------------RESUMEN------------------")
print(resumen)

#GUARDAR REPORTE EN EXCEL
try:
    df.to_excel('Reporte_inventario.xlsx', index=False)
    print("Reporte de Inventario guardado exitosamente en excel")
    
    #guardar el resumen en CSV
    resumen.to_csv('Resumen_Gamas.csv')
    print("Resumen de Gamas guardado exitosamente en CSV.")
except Exception as e:
    print(f"Error al guardar los archivos: {e}")    
    print("Asegurate de que el inventario no este abierto en este momento.")
