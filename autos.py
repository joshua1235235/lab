class Auto:
    def __init__(self, marca, modelo, año, color, motor, combustible, transmision, puertas, asientos, precio_compra):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.motor = motor
        self.combustible = combustible
        self.transmision = transmision
        self.puertas = puertas
        self.asientos = asientos
        self.precio_compra = precio_compra
        self.precio_venta = self.calcular_precio_venta()

    def calcular_precio_venta(self):
        return self.precio_compra * 1.4

    def mostrar_informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Precio de Venta: {self.precio_venta}"

# Ejemplo de uso
auto1 = Auto("Toyota", "Corolla", 2021, "Rojo", "2.0L", "Gasolina", "Automático", 4, 5, 20000)
print(auto1.mostrar_informacion())
