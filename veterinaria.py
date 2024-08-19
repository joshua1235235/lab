class Perro:
    def __init__(self, nombre, raza, edad, peso, color, historia_clinica, dueño, contacto):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.color = color
        self.historia_clinica = historia_clinica
        self.dueño = dueño
        self.contacto = contacto
        self.estado = "NO ATENDIDO"
        self.tipo = "Perro Grande" if peso >= 10 else "Perro Pequeño"

    def registrar_atencion(self):
        self.estado = "ATENDIDO"

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}, Estado: {self.estado}"

# Ejemplo de uso
perro1 = Perro("Fido", "Labrador", 3, 15, "Negro", "Historia limpia", "Juan", "123456789")
perro1.registrar_atencion()
print(perro1.mostrar_informacion())
