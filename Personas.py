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
        self.departamento = "data"
        self.puesto = "analyst"
           
    def presentation1(self):
            Persona.presentation(self),
            print(f"hola!, mi departamneto es {self.departamento} y mi puesto {self.puesto}")
          
        
       t1 = Trabajador('Alberto','23','Data','Developer')
       t1.presentation()
            
