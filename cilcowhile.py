#tambien los conocemos como el cliclo mientras (while)
#siempre se debe declarar una variable CENTINELA o de control para evaluar la ejecucion de mi Ciclo


i=0
resul=0
import math

#Menu de opciones
print("-----MENU-----")
print("1. SUMAR 2 NUMEROS.")
print("2. RESTAR 2 NUMEROS.")
print("3. ENCONTRAR LA RAIZ CUADRADA DE UN NUMERO.")
print("4. MULTIPLICAR 2 NUMEROS.")
print("5. Salir.")
while(i!=5):
    i=int (input("Digita una opción del Menú: "))
    if(i==1):
        num1 = int (input("Digita el primer número: "))
        num2 = int (input("Digita el segúndo número: "))
        resul=num1+num2
        print("la suma de ",num1," mas ",num2," es igual a ",resul)
    elif(i==2):
        num1 = int (input("Digita el primer número: "))
        num2 = int (input("Digita el segúndo número: "))
        resul=num1-num2
        print("la resta de ",num1," mas ",num2," es igual a ",resul)
    elif(i==3):
        num1 = int (input("Digita el primer número: "))
        resul=math.sqrt(num1)
        print("la raiz cuadrada de ",num1," es igual a ",resul)
    elif(i==4):
        num1 = int (input("Digita el primer número: "))
        num2 = int (input("Digita el segúndo número: "))
        resul=num1*num2
        print("la Multiplicacion de ",num1," por ",num2," es igual a ",resul)
    elif(i==5):
        break
    else:print("Digita una opción válida...")