class DispositivoElectronico:
    def __init__(self, nombre, tipo, marca, modelo, almacenamiento, precio_compra):
        self.nombre = nombre
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.almacenamiento = almacenamiento
        self.precio_compra = precio_compra
        self.precio_venta = self.calcular_precio_venta()

    def calcular_precio_venta(self):
        return self.precio_compra * 1.7

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}, Precio de Venta: {self.precio_venta}"

# Ejemplo de uso
dispositivo1 = DispositivoElectronico("Celular PHR", "Smartphone", "PHR", "X100", "128GB", 300)
print(dispositivo1.mostrar_informacion())
