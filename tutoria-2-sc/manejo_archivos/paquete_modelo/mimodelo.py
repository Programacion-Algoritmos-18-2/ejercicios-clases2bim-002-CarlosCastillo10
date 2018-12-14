"""
    creación de clases
"""

class Persona(object):
    """
    """
    
    def __init__(self, n, ape, ed, cod, n1, n2):
        """
            Atributos de la clase Persona.
        """
        self.nombre = n
        self.edad = int(ed)
        self.codigo = int(cod)
        self.apellido = ape
        self.nota1 = int(n1)
        self.nota2 = int(n2)

    def agregar_nombre(self, n):
        """
            Inicializa la varible nombre
        """
        self.nombre = n

    def obtener_nombre(self):
        """
            Retorna el valor que tenga la variable nombre
        """
        return self.nombre

    def agregar_edad(self, n):
        """
            Inicializa la varible edad
        """
        self.edad = int(n)

    def obtener_edad(self):
        """
            Retorna el valor que tenga la variable edad
        """
        return self.edad
    
    def agregar_codigo(self, n):
        """
            Inicializa la varible codigo
        """
        self.codigo = int(n)

    def obtener_codigo(self):
        """
            Retorna el valor que tenga la variable codigo
        """
        return self.codigo

    def agregar_apellido(self, ape):
        """
            Inicializa la varible apellido
        """
        self.apellido = ape
    
    def obtener_apellido(self):
        """
            Retorna el valor que tenga la variable apellido
        """
        return self.apellido

    def agregar_nota1(self, n1):
        """
            Inicializa la varible nota1
        """
        self.nota1 = n1

    def obtener_nota1(self):
        """
            Retorna el valor que tenga la variable nota1
        """
        return self.nota1

    def agregar_nota2(self, n2):
        """
            Inicializa la varible nota2
        """
        self.nota2 = n2

    def obtener_nota2(self):
        """
            Retorna el valor que tenga la variable nota2
        """
        return self.nota2

    # Modificamos el metodo str. 
    def __str__(self):
        """
        """
        return "%s - %s - %d - %d - %d - %d" % (self.obtener_nombre(), self.obtener_apellido(),\
                self.obtener_edad(), self.obtener_codigo(), self.obtener_nota1(), self.obtener_nota2())


class OperacionesPersona(object):
    """
    """
    
    def __init__(self, listado):
        """
        Constructor
        """
        self.listado_personas = listado

    def agregar_listado_personas(self, listado):
        """
        """
        self.listado_personas = listado

    def obtener_listado_personas(self):
        """
        """
        return self.listado_personas

    def obtener_promedio_n1(self):

        suma = 0 # Varibale inicializada
        
        for x in self.obtener_listado_personas():
            suma += x.obtener_nota1()
        
        return suma / len(self.obtener_listado_personas()) # Retorna el promedio


    def obtener_promedio_n2(self):

        suma = 0 # Varibale inicializada
        
        for x in self.obtener_listado_personas():
            suma += x.obtener_nota2()
        
        return suma / len(self.obtener_listado_personas()) # Retorna el promedio
    
    def obtener_listado_n1(self):
        
        cadena = " " # Varibale inicializada
        
        for x in self.obtener_listado_personas():
            if(x.obtener_nota1() < 15):
                cadena = "\t%s%s-%s-%d\n" %(cadena, x.obtener_nombre(), x.obtener_apellido(), x.obtener_nota1())
        
        return cadena # Retorna lo que contiene la varible cadena
    
    def obtener_listado_n2(self):
        
        cadena = " " # Varibale inicializada
        
        for x in self.obtener_listado_personas():
            if(x.obtener_nota2() < 15):
                cadena = "\t%s%s-%s-%d\n" %(cadena, x.obtener_nombre(), x.obtener_apellido(), x.obtener_nota2())
        
        return cadena # Retorna lo que contiene la varible cadena
    
    
    def obtener_listado_personas1(self, letra1, letra2):
        
        #cadena = ""
        lista = []
        for x in self.obtener_listado_personas():

            if(x.obtener_nombre()[0:1] == letra1 or x.obtener_nombre()[0:1] == letra2 ): # Compara la primera letra del nombre
                #cadena = "%s %s-%s\n\t" %(cadena, x.obtener_nombre(),x.obtener_apellido())
                lista.append(x.obtener_nombre())
        return lista


    def __str__(self):
            
        cadena = "" # Varibale inicializada
            
        for x in self.obtener_listado_personas():
                
            cadena = "%s-%s-%s\n" %(cadena, x.obtener_nombre(),x.obtener_apellido())
            
        return cadena # Retorna lo que contiene la varible cadena
