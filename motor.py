#MODULKE FOR CONTROL MOTOR 4WD - 2WD

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

pdr = GPIO.PWM(12, 1500)  # channel=12 frequency=1500Hz
piz = GPIO.PWM(18, 1500)  # channel=18 frequency=1500Hz
pdr.start(0)
piz.start(0)
GPIO.output(14, GPIO.LOW)
GPIO.output(15, GPIO.LOW)
GPIO.output(23, GPIO.LOW)
GPIO.output(24, GPIO.LOW)

def avanzar(vl1,vl2):
    pdr.ChangeDutyCycle(vl1)
    piz.ChangeDutyCycle(vl2)
    GPIO.output(14,GPIO.LOW)
    GPIO.output(15,GPIO.HIGH)
    GPIO.output(23,GPIO.LOW)
    GPIO.output(24,GPIO.HIGH)  
    #time.sleep(.1)
    print("avanzar")
def izquierda(vl1,vl2):
    pdr.ChangeDutyCycle(vl1)
    piz.ChangeDutyCycle(vl2)
    GPIO.output(14,GPIO.LOW)
    GPIO.output(15,GPIO.HIGH)
    GPIO.output(23,GPIO.HIGH)
    GPIO.output(24,GPIO.LOW)  
    print("izquierda")
def derecha(vl1,vl2):
    pdr.ChangeDutyCycle(vl1)
    piz.ChangeDutyCycle(vl2)
    GPIO.output(14,GPIO.HIGH)
    GPIO.output(15,GPIO.LOW)
    GPIO.output(23,GPIO.LOW)
    GPIO.output(24,GPIO.HIGH)            
    print("derecha")
def retroceso(vl1,vl2):
    pdr.ChangeDutyCycle(vl1)
    piz.ChangeDutyCycle(vl2)
    GPIO.output(14,GPIO.HIGH)
    GPIO.output(15,GPIO.LOW)
    GPIO.output(23,GPIO.HIGH)
    GPIO.output(24,GPIO.LOW)   
    print("retroceso")
def Stop():
    pdr.ChangeDutyCycle(0)
    piz.ChangeDutyCycle(0)
    GPIO.output(14,GPIO.HIGH)
    GPIO.output(15,GPIO.HIGH)
    GPIO.output(23,GPIO.HIGH)
    GPIO.output(24,GPIO.HIGH)   
    print("STOP")
