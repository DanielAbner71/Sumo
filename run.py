from sklearn.neural_network import MLPClassifier  
from random import randint
import rpyc
import pandas as pd

conn = rpyc.classic.connect('169.254.229.60') # host name or IP address of the EV3
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

def IA():
    global accion
    global degrees
    data = pd.read_csv('log3.csv') 

    x = data.drop('Label', axis=1).values
    y = data['Label'].values
 
    mlp = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=1000)  
    mlp.fit(x, y)

    while True:
        colorString = color.color_name
        distancia_value = distancia.distance_centimeters

        inputA=0
        
        if(colorString == 'Black'):
            inputA=0
        else:
            inputA=1

        Inputs = [[inputA, distancia_value]]
        mlpPrediction = mlp.predict(Inputs)

        if(mlpPrediction[0] == 'Buscando'):
            if(accion != "Buscando"):
                Caminar(20)
                accion = "Buscando"
            Defender(100)
        elif(mlpPrediction[0] == 'Atacar'):
            if(accion != "Atacar"):
                Caminar(40)
            Atacar(100)
        elif(mlpPrediction[0] == 'Encontrado'):
            if(accion != "Encontrado"):
                Encontrado(40)
            Defender(100)
        elif(mlpPrediction[0] == 'Esquivando'):
            EsquivarLimite()

        print(Inputs)
        print(degrees)
        print(mlpPrediction[0])

IA()