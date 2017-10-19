#!/usr/bin/python
# -*- encoding: utf-8 -*-

#######################################
# ###     Raúl Caro Pastorino     ### #
## ##                             ## ##
### # https://github.com/fryntiz/ # ###
## ##                             ## ##
# ###       www.fryntiz.es        ### #
#######################################

##############################
##    Importar Librerías    ##
##############################
import time  # Importamos la libreria time --> time.sleep
import RPi.GPIO as GPIO  # Importar librería para controlar hardware GPIO

##############################
##         Variables        ##
##############################
# Definiendo los pines que serán usados
LCD_RS = 7
LCD_E = 17
LCD_D4 = 27
LCD_D5 = 22
LCD_D6 = 23
LCD_D7 = 24

# Carácteres por línea → 16
LCD_WIDTH = 16
LCD_CHR = True
LCD_CMD = False

LINE_1 = 0x80 # LCD dirección en la RAM para la primera línea
LINE_2 = 0xC0 # LCD dirección en la RAM para la segunda línea

# Constantes de tiempo para retraso y actualización
E_PULSE = 0.0005
E_DELAY = 0.0005
