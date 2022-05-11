from class_empleado import Empleado


class Gerente(Empleado):
    def __init__(self,nombre,sueldo,departamento):
        super().__init__(self,nombre,sueldo)
        self._departamento = departamento

    def __str__(self):
        return f"Departamento: {self._departamento} GERENTE: {super().__str__()}"





geren = Gerente("sistemas","julio",50000)
print(geren)
