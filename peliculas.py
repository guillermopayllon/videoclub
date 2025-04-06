## Nuestro catálogo tendrá los siguientes parámetros:
# - Nombre:
# - Año de estreno:
# - Argumento:
# - Precio Alquiler:

#####################################################################

class Pelicula:
    def __init__(self, nombre, anio_estreno, argumento, precio_alquiler):
        self.nombre = nombre
        self.anio_estreno = anio_estreno
        self.argumento = argumento
        self.precio_alquiler = precio_alquiler

    def __str__(self):
        return f"{self.nombre} ({self.anio_estreno}) - {self.argumento} - Precio Alquiler: {self.precio_alquiler}"