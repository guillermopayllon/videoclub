## Este archivo va a contener todas nuestras funciones para el servicio de peliculas
# - agregar_pelicula
# - listar_peliculas
# - eliminar_pelicula
# - eliminar_archivo_peliculas

##########################################################################################

#Creamos la clase Pelicula
class Pelicula:
    def __init__(self):
        self.nombre_archivo = "peliculas.txt"
        
    # Definimos el método para agregar una película
    def agregar_pelicula(self, nombre, anio_estreno, argumento, precio_alquiler):
        with open(self.nombre_archivo, "a") as archivo:
            archivo.write(f"{nombre},{anio_estreno},{argumento},{precio_alquiler}\n")
        print(f"Pelicula '{nombre}' agregada exitosamente.")
        
    # Definimos el método para listar las películas
    def listar_peliculas(self):
        with open(self.nombre_archivo, "r") as archivo:
            peliculas = archivo.readlines()
            if not peliculas:
                print("No hay películas en el catálogo.")
                return
            print("Catálogo de Películas:")
            for pelicula in peliculas:
                nombre, anio_estreno, argumento, precio_alquiler = pelicula.strip().split(",")
                print(f"Nombre: {nombre}, Año: {anio_estreno}, Argumento: {argumento}, Precio Alquiler: {precio_alquiler}")
                
    # Definimos el método para eliminar una película
    def eliminar_pelicula(self, nombre):
        with open(self.nombre_archivo, "r") as archivo:
            peliculas = archivo.readlines()
        with open(self.nombre_archivo, "w") as archivo:
            for pelicula in peliculas:
                if pelicula.strip().split(",")[0] != nombre:
                    archivo.write(pelicula)
        print(f"Pelicula '{nombre}' eliminada exitosamente.")
        
    # Definimos el método para eliminar el archivo de películas
    def eliminar_archivo_peliculas(self):
        import os
        if os.path.exists(self.nombre_archivo):
            os.remove(self.nombre_archivo)
            print("Archivo de películas eliminado exitosamente.")
        else:
            print("El archivo de películas no existe.")
        
    