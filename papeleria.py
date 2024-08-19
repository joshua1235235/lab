class Item:
    def __init__(self, nombre, tipo, precio_compra):
        self.nombre = nombre
        self.tipo = tipo
        self.precio_compra = precio_compra
        self.precio_venta = self.calcular_precio_venta()

    def calcular_precio_venta(self):
        return self.precio_compra * 1.30

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}, Precio de Venta: {self.precio_venta}"

# Ejemplo de uso
cuaderno = Item("Cuaderno Hojitas", "100 hojas", 2.00)
lapiz = Item("Lápiz Rayas", "Grafito", 0.50)
print(cuaderno.mostrar_informacion())
print(lapiz.mostrar_informacion())
