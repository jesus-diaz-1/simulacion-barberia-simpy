# Simulacion de una barberia con SimPy

Este proyecto simula el funcionamiento de una barberia utilizando Python y la libreria SimPy.

## Objetivo

Representar el proceso de llegada, espera y atencion de clientes dentro de una barberia, considerando un numero limitado de barberos.

## Datos de entrada

El programa solicita al usuario:

- Numero de barberos
- Numero de clientes a simular
- Tiempo promedio entre llegadas
- Tiempo minimo de servicio
- Tiempo maximo de servicio

## Funcionamiento

Cada cliente llega a la barberia en un tiempo determinado.

Si existe un barbero disponible, el cliente comienza su servicio inmediatamente.

Si todos los barberos estan ocupados, el cliente entra en espera hasta que uno de ellos quede disponible.

El tiempo de servicio se genera dentro del rango indicado por el usuario.

## Resultados

Al finalizar la simulacion, el programa muestra:

- Clientes atendidos
- Clientes que tuvieron que esperar
- Tiempo promedio de espera
- Mayor tiempo de espera

## Requisitos

- Python 3
- SimPy

Para instalar SimPy:

```bash
pip install simpy