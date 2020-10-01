#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 09:08:50 2020

@author: msastre
"""

class Persona(object):
    def __init__ (self,nombre,edad):
        self.nombre = nombre
        self.edad=edad
        
    def presentation(self):
        print(f"Hola! Soy {self.nombre} y tengo {self.edad} años")
        
        

class Trabajador(Persona):
    
    #Constructor de la clase supervisor
    def __init__(self,nombre,edad,departamento,puesto):
        #Invocacion al constructor de la clase Persona
        Persona.__init__(self, nombre, edad)
        
        #4.Por defecto el departamento sea data y el puesto Analyst
        self.departamento = "data"
        self.puesto = "analyst"
           
    def presentation(self):
            Persona.presentation(self),
            print(f"hola!, mi departamneto es {self.departamento} y mi puesto {self.puesto}")
          
            
            
    
t1 = Trabajador('Alberto','23','Data','Developer')
t1.presentation()
        
 #3.Diferencia entre self.nombre y nombre 
'''La diferencia es el alcance o ámbito de la variable nombre. Si se declara la variable como self.nombre, entonces el ambito será
global, lo que implica que cualquiera que instancie esa clase tiene acceso a la variable nombre.
Por otr lado, si la variable es una variable local, definida como nombre únicamente será accesible desde el método donde se ha
declarado.'''

 

#5.
my_var_list = [ "Andrea", "42", "Ventas", "Manager"]

t2 = Trabajador(my_var_list[0],my_var_list[1],my_var_list[2],my_var_list[3])
t2.presentation()

#Salida
'''Hola! Soy Andrea y tengo 42 años
hola!, mi departamneto es data y mi puesto analyst'''


#6.Diccionarios

dictii = { "nombre": "Andrea", "edad": "42","departamento":"Ventas" , "puesto": "Manager"}

t2 = Trabajador(dictii['nombre'],dictii['edad'],dictii['departamento'],dictii['puesto'])
t2.presentation()







