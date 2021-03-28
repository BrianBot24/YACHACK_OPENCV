#MODULE for use of the PID Control
#Necessary to use motor.py

from motor import *

#INITIAL VALUES
derivativo= 0
proporcional= 0
integral = 0 
PID_= 0
lerror= 0 

def PID(error,Kp,Ki,Kd,vi):
    global derivativo
    global proporcional
    global integral
    global PID_
    global lerror
    
    proporcional= error
    integral= integral + lerror
    derivativo= error - lerror

    #if integral>1000:
        #integral=1000

    #if integral<-1000:
        #integral=-1000

    PID_= proporcional*Kp + integral*Ki + derivativo*Kd
    lerror = proporcional
    
    mdr= vi - PID_ #Right motor speed.
    miz= vi + PID_ #Left motor speed.
    
    if  mdr>100:
        mdr=100
    
    if mdr<0:
        mdr=0
    
    if  miz>100:
        miz=100
    
    if miz<0:
        mdr=0
    
    avanzar(miz,mdr)

    #print(proporcional)
    #print(integral)
    #print(derivativo)
    #print(PID_)
    #print("motor derecha",mdr)
    #print("motor izquierda",miz)
    #print(mdr+miz)

