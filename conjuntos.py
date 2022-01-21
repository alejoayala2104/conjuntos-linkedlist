#!/usr/bin/env python

from ed.secuenciales.listaSE import ListaSE

"""Un conjunto es una secuencia de elementos, todos ellos del mismo tipo sin
duplicidades. En este módulo se implementa la clase Conjunto, para evaluar la
utilización de la librería 'ed.secuenciales.listaSE'
Author : ANDRÉS ALEJANDRO AYALA CHAMORRO
"""

class Conjunto:
    """Esta clase representa e identifica a un conjunto de cualquier tipo de
    dato. Su implementación se realiza a través de una lista simplemente
    enlazada
    """
    def __init__(self, nombre):
        """Constructor de la clase Conjunto
        Parameters
        ----------
        nombre : str
        El nombre que identifica al conjunto. Siempre en mayúscula, por norma de los conjuntos.

        lista: ListaSE
        El conjunto de elementos representados por una lista simplemente enlazada
        """
        
        self.nombre = nombre.upper()
        self.lista = ListaSE()

    def agregar(self, *parámetro_consulta):
        """Método que permite agregar cualquier cantidad de elementos del mismo
        tipo al conjunto, validando además que no se encuentren repetidos.
        Ejm: Para adicionar los números enteros 4, 78, 5 y 10
        al conjunto A sería de la forma:
        conjuntoA.agregar(4, 78, 5, 10)
        Es posible adicionar al mismo conjunto el valor 7 y 10 de la forma:
        conjuntoA.agregar(7, 10)
        En el caso de imprimir el conjunto A el resultado sería:
        'A = {4, 78, 5, 10, 7}'
        Parameters
        ----------
        *parámetro_consulta : Parametro que representa cualquier tipo de elemento a agregar en el conjunto. Recibe uno o más elementos. 
        """
        # for elemento in parámetro_consulta:
        #     if parámetro_consulta.count(elemento) > 1:
        #         print("Un conjunto no puede tener elementos repetidos")
        #         return
        
        for elemento in parámetro_consulta:
            if(self.lista.buscar(elemento) is None):
                self.lista.adicionar(elemento)
                        

    def cardinal(self):
        """Método que representa al número de elementos que tiene un conjunto.
        Cardinal (D)= n (D)= número de elementos.
        Ejm: El número Cardinal del conjunto D = {8, 15, -85, 26, 19} es = 5
        Returns
        -------
        int
        Número de elementos del conjunto
        """
        
        return len(self.lista)

    def pertenencia(self, un_elto):
        """Se dice que todo elemento de un conjunto pertenece a dicho conjunto
        si forma parte del conjunto en mención y para indicar esto lo
        representamos de la siguiente manera ∈ y en contrario de no
        pertenencia ∉
        Ejm: Si tenemos A = {7, 25, 32, 10}
        Se dice que 32 ∈ A: Se lee '32 pertenece al conjunto A'
        y también se dice que 14 ∉ A: Se lee '14 no pertenece al conjunto A'
        Parameters
        ----------
        un_elto : object
        Un valor, del mismo tipo de los elementos del conjunto, que se
        analiza si pertenece o no al conjunto
        Returns
        -------
        bool
        Verdadero, si 'un_elto' pertenece al conjunto. Falso, en caso contrario
        """
        
        if self.lista.buscar(un_elto):
            return True
        else:
            return False

    def es_subconjunto(self, otro_cjto):
        """En general si A y B son dos conjuntos cualesquiera, decimos que B es
        un subconjunto de A si todo elemento de B lo es de A también.
        Sean los conjuntos A = {0, 1, 2, 3, 5, 8} y B = {1, 2, 5}
        Decimos que B esta contenido en A, o que B es un subconjunto de A
        Parameters
        ----------
        otro_cjto : Conjunto
        El conjunto con el cual se compara y se determina si todos los
        elementos del conjunto estan en ese conjunto
        Returns
        -------
        bool
        Verdadero, si todos los elementos de conjunto forman parte de
        'otro_conjunto'. Falso, en caso contrario
        """
        
        es_subconj = True # Se asume que si es subconjunto

        for nodo in self.lista:
            elemento = nodo.dato
            if (otro_cjto.lista.buscar(elemento)) is None:
                # En caso de no encontrar algún elemento de otro_cjto en el conjunto self, otro_cjto no es subconjunto de self
                es_subconj = False
        return es_subconj
    
    def union(self, otro_cjto):
        """La unión de conjuntos A y B es el conjunto formado por los elementos
        que pertenecen a A, a B o a ambos
        Sean los conjuntos A = {10, 14, 32} y B = {1, 2, 5}
        A ∪ B = {10, 14, 32, 1, 2, 5}
        Parameters
        ----------
        otro_cjto : Conjunto
        El conjunto con el cual se realiza la unión
        Returns
        -------
        Conjunto
        Un nuevo conjunto que tendrá como nombre:
        'nombre_conjunto U nombre_otro_conjunto'
        y que contendrá los elementos producto de la unión entre ambos
        """
        nom_cjto_union = str(self.nombre) + " U " + str(otro_cjto.nombre)
        cjto_union = Conjunto(nom_cjto_union)
        cjto_union.lista = ListaSE()

        # Primero copio el conjunto self al conjunto unión
        for nodo in self.lista:
            cjto_union.agregar(nodo.dato)

        for nodo in otro_cjto.lista:
            elemento = nodo.dato
            if self.lista.buscar(elemento) is None:           
                cjto_union.agregar(elemento)

        return cjto_union

    def intersection(self, otro_cjto):
        """Dados lo conjuntos A y B, se llama intersección al conjunto formado
        por los elementos que pertenecen a A y B a la vez; es decir, es el
        conjunto formado por los elementos comunes a A y B.
        Sean los conjuntos A = {5, 12, 28, 6} y B = {6, 50, 12, 77}
        A ∩ B = {12, 6}
        Parameters
        ----------
        otro_cjto : Conjunto
        El conjunto con el cual se realiza la intersección
        Returns
        -------
        Conjunto
        Un nuevo conjunto que tendrá como nombre:
        'nombre_conjunto I nombre_otro_conjunto'
        y que contendrá los elementos producto de la intersección entre
        ambos
        """

        nom_cjto_inter = str(self.nombre.upper()) + " I " + str(otro_cjto.nombre.upper())
        cjto_inter = Conjunto(nom_cjto_inter)

        for nodo in self.lista:
            elemento = nodo.dato
            if otro_cjto.lista.buscar(elemento):
                cjto_inter.agregar(elemento)
        
        return cjto_inter

    def diferencia(self, otro_cjto):
        """Sean A y B dos conjuntos. La diferencia de A y B se denota por A-B y
        es el conjunto de los elementos de A que no están en B
        Sea A = {5, 10, 15, 20} y B = {25, 5, 15, -21, 30, 17}
        A - B = {10, 20}
        Parameters
        ----------
        otro_cjto : Conjunto
        El conjunto con el cual se realiza la diferencia
        Returns
        -------
        Conjunto
        Un nuevo conjunto que tendrá como nombre:
        'nombre_conjunto - nombre_otro_conjunto'
        y que contendrá los elementos producto de la diferencia entre
        ambos
        """
        
        nom_cjto_dif = str(self.nombre.upper()) + " - " + str(otro_cjto.nombre.upper())
        cjto_dif = Conjunto(nom_cjto_dif)

        for nodo in self.lista:
            elemento = nodo.dato
            if not otro_cjto.lista.buscar(elemento): #Si no lo encuentra, añadalo al nuevo cjto.
                cjto_dif.agregar(elemento)

        return cjto_dif


    def __str__(self):
        """Devuelve una cadena con la presentación del conjunto
        Returns
        -------
        str
        Una cadena con la presentación del conjunto, en el formato:
        'NOMBRE_DEL_CONJUNTO_EN_MAYUS = {elemento1, elemento2, elementoN}'
        Ejms: 'A = {45, 78, 30}', 'C U D = {10, 8, 7, 12, 100}',
        'B I C = {4, 0, 8}', 'D - A = {34, 6}'
        """
        
        cadena = str(self.nombre) + " = {"
        for nodo in self.lista:
            if nodo: # Si el nodo actual es diferente de None
                cadena += str(nodo.dato)
                if nodo.sig is None:
                    pass
                else:
                    cadena += "," # Añade otra coma
        
        cadena += "}"
        return cadena