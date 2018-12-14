from paquete_archivos.miarchivo import MiArchivo
from paquete_modelo.mimodelo import Persona, OperacionesPersona

m = MiArchivo()
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]

# print(lista)

lista = lista[1:]
lista_personas = []

for d in lista:
    p = Persona(d[1], d[2], d[3], d[0],d[4],d[5])
    lista_personas.append(p)

operaciones = OperacionesPersona(lista_personas)

print("\nPromedio de la nota 1: %.1f " %operaciones.obtener_promedio_n1())

print("Promedio de la nota 2: %.1f" %operaciones.obtener_promedio_n2())

print("\nEl listado de personas cuya nota1 es menor a 15 es: \n\n%s" %operaciones.obtener_listado_n1()) # que retorne los personas con notas1\
       
print("\nEl listado de personas cuya nota2 es menor a 15 es: \n\n%s" %operaciones.obtener_listado_n2()) # que retorne los personas con notas2\

print("\nEl listado de personas cuyo nombre empieza con 'R' o 'J' es: \n\n\t%s" %operaciones.obtener_listado_personas1("R", "J")) # que retorne listado de personas
