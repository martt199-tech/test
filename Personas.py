#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 09:08:50 2020

@author: msastre
"""

class Persona:
    def __init__ (self,nombre,edad):
        self.nombre = nombre
        self.edad=edad
        
    def presentation(self):
        print(f"Hola! Soy {self.nombre} y tengo {self.edad} años")
        
        