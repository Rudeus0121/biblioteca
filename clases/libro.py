import autor
import editorial_libro
class libro(autor, editorial_libro):
    def __init__(self,id_libro,ISBN,nombre_libro,id_autor,id_editorial):
            autor().__init__(id_autor)
            editorial_libro().__init__(id_editorial)
            self.ISBN = ISBN
            self.id_libro = id_libro
            self.nombre_libro = nombre_libro

