#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 12:38:09 2020

@author: msastre
"""
from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults
from datetime import datetime, date, timedelta

class TimeDiff(BaseOperator):

    @apply_defaults
    def __init__(
            self,
            date: date,
            *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.date = date
  
    def execute(self, context):
        
        date_dada = datetime.strptime(self.date, '%Y-%m-%d')
        date_system = datetime.now.date()
       if str(fecha_final) < str(fecha):
           print f" {fecha_final} Es menor que {fecha}"
       else:
           print f" {fecha_final} Es menor que {fecha}"
  