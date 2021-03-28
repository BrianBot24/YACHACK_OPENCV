middleX= 620 #Center of the image (my webcam is 1240x720)

#INIT VALUES
derivativo= 0
proporcional= 0
integral= 0
PID_= 0
lerror= 140 #For practical purposes it is given a value, it starts with 0 in the real code

cX= 466 #Value (Found with the center of the line or center of mass (findContours de OPENCV))

vi= 70               #MAX speed of motors in a straight line, can be from 40 to 80
Kp= (100-vi)/middleX #Value between 0.096 to 0.032
Kd= 0.0167 #Value for demonstration purposes, it has to be calibrated in each robot
Ki= 0.002  #Value for demonstration purposes, it has to be calibrated in each robot

error= cX - middleX # 

proporcional= error
integral= integral + lerror
derivativo= error - lerror

#if integral>1000:
    #integral=1000

#if integral<-1000:
    #integral=-1000

PID_= proporcional*Kp + integral*Ki + derivativo*Kd

mdr= vi - PID_ #Right engine speed
miz= vi + PID_ #Left engine speed

lerror = proporcional

print(proporcional)
print(integral)
print(derivativo)
print(PID_)
print(mdr)
print(miz)
print(mdr+miz)
