import usuario
class prestamo(usuario):
    def __init__(self, id_prestamo, id_usuario, fecha_prestamo, fecha_devolucion):
        super().__init__(id_usuario)
        self.id_prestamo = id_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def calcular_fecha():
        pass