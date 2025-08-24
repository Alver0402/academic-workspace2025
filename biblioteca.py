from typing import List
from datetime import date


class Libro:
    def __init__(self, isbn: str, titulo: str, autor: str):
        
        self.isbn = isbn
        self.ISBN = isbn
        self.titulo = titulo
        self.autor = autor

    def getISBN(self):
        return self.isbn

    def getTitulo(self):
        return self.titulo

    def getAutor(self):
        return self.autor



class Estudiante:
    def __init__(self, codigo_estudiante: str, nombres: str, apellidos: str):
       
        self.codigo_estudiante = codigo_estudiante
        self.codigoEstudiante = codigo_estudiante  
        self.nombres = nombres
        self.apellidos = apellidos

    def getCodigo(self):
        return self.codigo_estudiante

    def getNombres(self):
        return self.nombres

    def getApellidos(self):
        return self.apellidos



class Prestamo:
    def __init__(self, id_prestamo: int, id_libro: str, codigo_estudiante: str,
                 fecha_prestamo: date, fecha_devolucion: date):
        
        self.id_prestamo = id_prestamo
        self.idPrestamo = id_prestamo

        self.id_libro = id_libro
        self.idLibro = id_libro

        self.codigo_estudiante = codigo_estudiante
        self.codigoEstudiante = codigo_estudiante

        self.fecha_prestamo = fecha_prestamo
        self.fechaPrestamo = fecha_prestamo

        self.fecha_devolucion = fecha_devolucion
        self.fechaDevolucion = fecha_devolucion

    def getIdPrestamo(self):
        return self.id_prestamo

    def getIdLibro(self):
        return self.id_libro

    def getCodigoEstudiante(self):
        return self.codigo_estudiante

    def getFechaPrestamo(self):
        return self.fecha_prestamo

    def getFechaDevolucion(self):
        return self.fecha_devolucion



class Biblioteca:
    def __init__(self):
        self.libros: List[Libro] = []
        self.estudiantes: List[Estudiante] = []
        self.prestamos: List[Prestamo] = []

    def agregarLibro(self, libro: Libro):
        self.libros.append(libro)

    def listarLibros(self):
        print("\n📚 Lista de Libros:")
        if not self.libros:
            print("No hay libros registrados.")
            return
        for libro in self.libros:
            print(f"ISBN: {libro.getISBN()} | Título: {libro.getTitulo()} | Autor: {libro.getAutor()}")

    
    def agregarEstudiante(self, estudiante: Estudiante):
        self.estudiantes.append(estudiante)

    def listarEstudiantes(self):
        print("\n👩‍🎓 Lista de Estudiantes:")
        if not self.estudiantes:
            print("No hay estudiantes registrados.")
            return
        for est in self.estudiantes:
           
            print(f"Código: {est.getCodigo()} - Nombre: {est.getNombres()} {est.getApellidos()}")

   
    def agregarPrestamo(self, prestamo: Prestamo):
        self.prestamos.append(prestamo)

    def listarPrestamos(self):
        print("\n📖 Lista de Préstamos:")
        if not self.prestamos:
            print("No hay préstamos registrados.")
            return
        for prestamo in self.prestamos:
            print(f"ID Préstamo: {prestamo.getIdPrestamo()} - "
                  f"Libro: {prestamo.getIdLibro()} - "
                  f"Estudiante: {prestamo.getCodigoEstudiante()} - "
                  f"Fecha Préstamo: {prestamo.getFechaPrestamo()} - "
                  f"Fecha Devolución: {prestamo.getFechaDevolucion()}")