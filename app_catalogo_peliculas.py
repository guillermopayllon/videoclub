#Este archivo va a contener el menú de la aplicación y la lógica de interacción con el usuario.
# # - mostrar_menu
# # - ejecutar_opcion
# # - main
##############################################################################

import servicio_peliculas
import os
import peliculas


class AppCatalogoPeliculas:
    def __init__(self, servicio_peliculas):
        self.servicio_peliculas = servicio_peliculas

    def mostrar_menu(self):
        print("Bienvenido al Catálogo de Películas")
        print("1. Agregar Película")
        print("2. Listar Películas")
        print("3. Eliminar Película")
        print("4. Eliminar Archivo de Películas")
        print("5. Salir")

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            nombre = input("Ingrese el nombre de la película: ")
            anio_estreno = input("Ingrese el año de estreno: ")
            argumento = input("Ingrese el argumento: ")
            precio_alquiler = input("Ingrese el precio de alquiler: ")
            self.servicio_peliculas.agregar_pelicula(nombre, anio_estreno, argumento, precio_alquiler)
        elif opcion == 2:
            self.servicio_peliculas.listar_peliculas()
        elif opcion == 3:
            nombre = input("Ingrese el nombre de la película a eliminar: ")
            self.servicio_peliculas.eliminar_pelicula(nombre)
        elif opcion == 4:
            self.servicio_peliculas.eliminar_archivo_peliculas()
        elif opcion == 5:
            print("Saliendo del catálogo...")
            return False
        else:
            print("Opción inválida. Intente nuevamente.")
        return True

    def main(self):
        while True:
            self.mostrar_menu()
            opcion = int(input("Seleccione una opción: "))
            if not self.ejecutar_opcion(opcion):
                break
if __name__ == "__main__":
      # Asegúrate de que el nombre del archivo sea correcto

    app = AppCatalogoPeliculas(servicio_peliculas=servicio_peliculas.Pelicula())
    app.main()