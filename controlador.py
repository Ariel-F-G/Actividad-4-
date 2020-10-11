import time
from modelo import num # se trae el archivo donde se almaceno el número ingresado por el usuario
a=num
factorial = 1
for i in range (a): #se establece el ciclo y el rengo del factorial a calcular
    factorial = factorial * a
    a = a -1  
print("El factorial es.") # nos indica el factorial del n+umero solicitado
time.sleep(1)
print (factorial) # muesta el resultado  
time.sleep(1)  
print("Desea ver la secuencia.") # se pregunta si se desea ver la secuencia del factorial
time.sleep(1)
print("""
1 si
2 no
""") # menu para seleccionar si se desea ver la secuencia
sec = (int(input()))  # se ingresa la respuesta del menu solicitado
from modelo import num # se trae el archivo  donde se guardo el número ingresado por el usuario
b=num
a=b
factorial = 1
if (sec==1): # se establece la condición  de selección del menu
    for i in range (a):  #se establece el ciclo y el rengo del factorial a calcular
        factorial *= a
        a= a-1
        print(factorial,"*",a) # se indica la secuencia del proceso del factorial
elif (sec==2):# se establece la condición  de selección del menu
    print("Te perdiste de ver las maravillas de la matemática ") 
    time.sleep(1)
    print("Te invitamos a realizar nuevamente el ejercicio y ver la secuencia")
elif (sec!= 1 and 2):
    print ("ingresó un caracter invalido")
    time.sleep(1)
    print("por favor siga las instruciones al pie de la letra")
