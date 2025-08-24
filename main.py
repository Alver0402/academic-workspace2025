from biblioteca import Biblioteca, Libro, Estudiante, Prestamo
from datetime import datetime
import biblioteca as _biblioteca  

def mostrar_menu():
    print("\n========= 📚 MENÚ BIBLIOTECA =========")
    print("1. Agregar libro")
    print("2. Listar libros")
    print("3. Registrar estudiante")
    print("4. Listar estudiantes")
    print("5. Registrar préstamo")
    print("6. Listar préstamos")
    print("0. Salir")
    print("======================================")

def main():
    biblio = Biblioteca()
    id_prestamo_counter = 1  

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            isbn = input("Ingrese ISBN: ")
            titulo = input("Ingrese título: ")
            autor = input("Ingrese autor: ")
            libro = Libro(isbn, titulo, autor)
            biblio.agregarLibro(libro)
            print("✅ Libro agregado con éxito.")

        elif opcion == "2":
            biblio.listarLibros()

        elif opcion == "3":
            codigo = input("Ingrese código del estudiante: ")
            nombres = input("Ingrese nombres: ")
            apellidos = input("Ingrese apellidos: ")
            estudiante = Estudiante(codigo, nombres, apellidos)
            
            print("[DEBUG] atributos del estudiante recién creado:", vars(estudiante))
            biblio.agregarEstudiante(estudiante)
            print("✅ Estudiante registrado con éxito.")

        elif opcion == "4":
            biblio.listarEstudiantes()

        elif opcion == "5":
            if not biblio.libros:
                print("⚠️ No hay libros disponibles para préstamo.")
                continue
            if not biblio.estudiantes:
                print("⚠️ No hay estudiantes registrados.")
                continue

            print("\n📚 Libros disponibles:")
            for i, libro in enumerate(biblio.libros, start=1):
                print(f"{i}. {libro.getTitulo()} ({libro.getISBN()})")

            libro_idx = int(input("Seleccione el número de libro: ")) - 1
            libro = biblio.libros[libro_idx]

            print("\n👩‍🎓 Estudiantes registrados:")
            for i, est in enumerate(biblio.estudiantes, start=1):
                print(f"{i}. {est.getNombres()} {est.getApellidos()} ({est.getCodigo()})")

            est_idx = int(input("Seleccione el número de estudiante: ")) - 1
            estudiante = biblio.estudiantes[est_idx]

            fecha_prestamo = input("Ingrese fecha de préstamo (dd/mm/aaaa): ")
            fecha_devolucion = input("Ingrese fecha de devolución (dd/mm/aaaa): ")

            try:
                fecha_prestamo_dt = datetime.strptime(fecha_prestamo, "%d/%m/%Y").date()
                fecha_devolucion_dt = datetime.strptime(fecha_devolucion, "%d/%m/%Y").date()
            except ValueError:
                print("⚠️ Formato de fecha inválido. Use dd/mm/aaaa.")
                continue

            prestamo = Prestamo(id_prestamo_counter, libro.getISBN(), estudiante.getCodigo(),
                                fecha_prestamo_dt, fecha_devolucion_dt)
            biblio.agregarPrestamo(prestamo)
            id_prestamo_counter += 1
            print("✅ Préstamo registrado con éxito.")

        elif opcion == "6":
            biblio.listarPrestamos()

        elif opcion == "0":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("⚠️ Opción no válida, intente de nuevo.")


if __name__ == "__main__":

    main()