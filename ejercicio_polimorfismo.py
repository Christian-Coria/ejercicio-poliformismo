from class_empleado import Empleado
from class_gerente import Gerente

# creando objetos de las clases con polimorfismo 
# este metodo imprime el detalle de los objetos ejecutando el metodo str de 
# cualquiera de los objetos de clase empleada o gerente 

def imprimir_detalle(objeto):
    print(objeto)
    print(type(objeto )) #para saber cual es el objeto y su metodo str que s ejecuta

#creamos los objetos

empleado1 = Empleado("juan", 50000) #esta variable empleado1 apunta al objeto de Empleado y su metodo str
#llamamos a la funcion
imprimir_detalle(empleado1)
gerente1 = Gerente("ju",5000,"sistemas")
imprimir_detalle(gerente1)