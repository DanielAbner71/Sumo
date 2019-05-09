#!/usr/bin/env python3
""" from ev3dev2.motor import LargeMotor, Motor, OUTPUT_A, OUTPUT_D, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import UltrasonicSensor, ColorSensor
from ev3dev2.led import Leds """
from threading import Thread
from random import randint
from sklearn.tree import DecisionTreeClassifier
import rpyc
import pandas as pd
conn = rpyc.classic.connect('169.254.152.137') # host name or IP address of the EV3
bgsrv = rpyc.BgServingThread(conn) #sleep removed

sensors = conn.modules['ev3dev2.sensor.lego']
motor = conn.modules['ev3dev2.motor']

distancia = sensors.UltrasonicSensor()
color = sensors.ColorSensor()

llantaIzq = motor.LargeMotor(motor.OUTPUT_D)
llantaDer = motor.LargeMotor(motor.OUTPUT_A)

llantas = motor.MoveTank(motor.OUTPUT_A, motor.OUTPUT_D)

rampa = motor.Motor(motor.OUTPUT_B)

accion = " "


degrees=0
maxDegrees=10

def Caminar(Speed):
    llantas.on(Speed, Speed)

def Detener():
    llantas.off()

def Atras(velocidad, rotaciones):
    llantas.on_for_rotations(motor.SpeedPercent(-velocidad),motor.SpeedPercent(-velocidad), rotaciones)

def GirarDerecha(velocidad, rotaciones):
    llantas.on_for_rotations(motor.SpeedPercent(-velocidad),motor.SpeedPercent(velocidad), rotaciones)

def GirarIzquierda(velocidad, rotaciones):
    llantas.on_for_rotations(motor.SpeedPercent(velocidad),motor.SpeedPercent(-velocidad), rotaciones)

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

    degrees=degrees+1

    if(degrees > maxDegrees):
        degrees=maxDegrees

    if(degrees == maxDegrees):
        rampa.off()
    else:
        rampa.on(-Speed)
        accion = "Atacar"

def Defender(Speed):
    global degrees

    degrees=degrees-1

    if(degrees < 0):
        degrees=0

    if(degrees <= 0):
        rampa.off()
    else:
        rampa.on(Speed)

def Encontrado(speed):
    global accion
    accion = "Encontrado"
    Caminar(speed)

def EsquivarLimite():
    global accion
    accion = "Esquivando"
    Detener()
    Atras(50, 1)
    Girar(80, 0.75)

def DetenerTodo():
    llantas.off()
    rampa.off()

def Buscar():
    global accion
    global degrees
    
    while True:

        colorString = color.color_name

        distancia_value = distancia.distance_centimeters

        if (distancia_value <= 15):
            if(accion!="Atacar"):
                Caminar(60)
            Atacar(100)
        elif (distancia_value <= 30):
            if(accion!="Encontrado"):
                Encontrado(50)
            Defender(50)
        else:
            if(accion!="Buscando"):
                Caminar(40)
                accion = "Buscando"
            Defender(100)

        if(colorString == 'Black'):
            EsquivarLimite()

        if(colorString == 'Red'):
            DetenerTodo()
            break

def IA():
    global accion
    global degrees

    df = pd.read_csv('log.csv')
    #Inputs
    X = df.drop('Label', axis=1).values
    #Classes
    y = df['Label'].values

    dt = DecisionTreeClassifier(max_depth=5)

    dt.fit(X, y)

    while True:
        colorString = color.color_name
        distancia_value = distancia.distance_centimeters

        inputA=0
        
        if(colorString == 'Black'):
            inputA=0
        else:
            inputA=1

        Inputs = [[inputA, distancia_value]]
        dtPrediction = dt.predict(Inputs)

        if(dtPrediction[0] == 'Buscando'):
            if(accion != "Buscando"):
                Caminar(20)
                accion = "Buscando"
            Defender(100)
        elif(dtPrediction[0] == 'Atacar'):
            if(accion != "Atacar"):
                Caminar(40)
            Atacar(100)
        elif(dtPrediction[0] == 'Encontrado'):
            if(accion != "Encontrado"):
                Encontrado(40)
            Defender(100)
        elif(dtPrediction[0] == 'Esquivando'):
            EsquivarLimite()

        print(Inputs)
        print(degrees)
        print(dtPrediction[0])


def GetDatos():
    datos = " "
    global accion
    global degrees

    while True:
        log = open("log.txt", "a")
        distancia_value= str(distancia.distance_centimeters)
        #Guardar datos en una variable
        datos = color.color_name+ "," + distancia_value + "," + accion
        print(datos)
        #Escribir los datos en el log
        log.write(datos + '\n')
        log.close()

        if(color.color_name == 'Red'):
            DetenerTodo()
            break

def Main():
    t1 = Thread(target = Buscar)
    t2 = Thread(target = GetDatos)

    t1.start()
    t2.start()

IA()