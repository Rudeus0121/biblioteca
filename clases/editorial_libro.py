import libro
class editorial_libro(libro):
    def __init__(self,id_editorial, ISBN, nombre_editorial,año_inicio,correo_E, telefono_E):
        super().__init__(ISBN)
        self.id_editorial = id_editorial
        self.nombre_editorial = nombre_editorial
        self.año_inicio = año_inicio
        self.correo_E = correo_E
        self.telefono_E = telefono_E
    
    def validar_correo():
        pass
