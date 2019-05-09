#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, Motor, OUTPUT_A, OUTPUT_D, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import UltrasonicSensor, ColorSensor
from ev3dev2.led import Leds
from threading import Thread
from random import randint

distancia = UltrasonicSensor()
color = ColorSensor()

llantaIzq = LargeMotor(OUTPUT_D)
llantaDer = LargeMotor(OUTPUT_A)

llantas = MoveTank(OUTPUT_A, OUTPUT_D)

rampa = Motor(OUTPUT_B)

accion = " "

degrees=0
maxDegrees=800

def Caminar(Speed):
    llantas.on(Speed, Speed)

def Detener():
    llantas.off()

def Atras(velocidad, rotaciones):
    llantas.on_for_rotations(SpeedPercent(-velocidad),SpeedPercent(-velocidad), rotaciones)

def GirarDerecha(velocidad, rotaciones):
    llantas.on_for_rotations(SpeedPercent(-velocidad),SpeedPercent(velocidad), rotaciones)

def GirarIzquierda(velocidad, rotaciones):
    llantas.on_for_rotations(SpeedPercent(velocidad),SpeedPercent(-velocidad), rotaciones)

def Girar(velocidad, rotaciones):
    randomNumb = randint(0, 1)
    if(randomNumb == 0):
        GirarDerecha(velocidad, rotaciones)
    else:
        GirarIzquierda(velocidad, rotaciones)
    
def Atacar(Speed):
    global accion
    global degrees
    global maxDegrees

    Caminar(100)

    degrees=degrees+1

    if(degrees > maxDegrees):
        degrees=maxDegrees

    if(degrees == maxDegrees):
        rampa.off()
    else:
        rampa.on(-Speed)
        accion = "Atacar"

def Defender(Speed):
    #global accion
    global degrees

    degrees=degrees-1

    if(degrees < 0):
        degrees=0

    if(degrees <= 0):
        rampa.off()
    else:
        rampa.on(Speed)
        #accion = "Defendiendo"

def Encontrado(speed):
    global accion
    accion = "Encontrado"
    Caminar(speed)
    Defender(100)

def EsquivarLimite():
    global accion
    accion = "Esquivando"
    Detener()
    Atras(50, 1)
    Girar(30, 0.75)

def Buscar():
    global accion
    global degrees
    
    while True:
        distancia_value= str(distancia.distance_centimeters)
        if (float(distancia_value) <= float(15)):
            Atacar(100)
        elif (float(distancia_value) <= float(30)):
            Encontrado(90)
        else:
            Caminar(70)
            Defender(100)
            accion = "Buscando"
            
        if(color.color_name == 'Black'):
            EsquivarLimite()

def GetDatos():
    datos = " "
    global accion
    global degrees

    while True:
        log = open("log.txt", "a")
        distancia_value= str(distancia.distance_centimeters)
        #Guardar datos en una variable
        datos = color.color_name+ "," + distancia_value + "," + accion
        #print(datos)
        #Escribir los datos en el log
        log.write(datos + '\n')
        log.close()

def Main():
    t1 = Thread(target = Buscar)
    t2 = Thread(target = GetDatos)

    t1.start()
    t2.start()
    
Main()