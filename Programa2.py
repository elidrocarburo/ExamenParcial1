import pandas as pd

arregloP= []
arregloP2= []

Producto = int(input("¿Cuántos productos desea agregar?: "))
for i in range(Producto):
    ProduNom = input("Ingrese el nombre de producto ")
    PrecioNum = float(input("¿Cuál es su precio?: "))

    arregloP.append(ProduNom)
    arregloP2.append(PrecioNum)

tabla = pd.DataFrame({
    "Nombre del producto": arregloP,
    "Precio del producto": arregloP2
})

print("       Tabla de productos y precios")
print(tabla)
