middleX= 620 #Centro de la imagen (para el caso de mi camaraweb es de 1240x720)

#VALORES INICIALES
derivativo= 0
proporcional= 0
integral= 0
PID_= 0
lerror= 140 # Para fines practicos se le da un valor, se inicia con 0 en el codigo real

cX= 466 #Valor de error(Se halla con el centro de la linea o centro de masa (findContours de OPENCV))

vi= 70 # velocidad MAX de los motores en linea recta, puede ser de 40 a 80
Kp= (100-vi)/middleX # valor entre 0.096 a 0.032
Kd= 0.0167 # valor apra fin demostrativo, se tiene que calibrar en cada robot
Ki= 0.002  # valor apra fin demostrativo, se tiene que calibrar en cada robot

error= cX - middleX # error entre el pixel central con el de la linea negra

proporcional= error
integral= integral + lerror
derivativo= error - lerror

#if integral>1000:
    #integral=1000

#if integral<-1000:
    #integral=-1000

PID_= proporcional*Kp + integral*Ki + derivativo*Kd

mdr= vi - PID_ #velocidad de motor derecho
miz= vi + PID_ #Velocidad de motor izquierda

lerror = proporcional

print(proporcional)
print(integral)
print(derivativo)
print(PID_)
print(mdr)
print(miz)
print(mdr+miz)
