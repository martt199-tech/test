#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 12:31:12 2020

@author: msastre
"""
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
'owner': 'airflow',
'depends_on_past': False,
'retries': 1,
'retry_delay': timedelta(seconds=5)
}

#1.Define un DAG que se ejecute todos los dias a las 3:00 a partir de hoy
with DAG(
        'my_first_Dag',
        start_date= datetime.datetime(2020,10, 3,3,00,00),
        schedule_interval='@date',
        default_args=default_args
        ) as dag:
#2.Crea las tareas dummy End and start
    start = DummyOperator('start')
    end = DummyOperator('end')
    start >> end # Define dependencies

