import libro
class detalle_libro(libro):
    def __init__(self, id_detalle_libro, id_libro, genero, n_paginas, stock_disponible):
        super().__init__(id_libro)
        self.id_detalle_libro = id_detalle_libro
        self.genero = genero
        self.n_paginas = n_paginas
        self.stock_disponible = stock_disponible
    
    def validar_stock():
        pass