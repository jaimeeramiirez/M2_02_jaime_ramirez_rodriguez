#EJERCICIO 1.- He creado 5 variables diferentes con valores ya establecidos. Luego he creado la variable solución que engloba la media aritmética de las 5 y la imprime en la pantalla.
x1=8
x2=7
x3=9
x4=9
x5=6
sol =(((x1+x2+x3+x4+x5)/5))
print("La nota media es", sol)
print("\n")

#EJERCICIO 2.- La variable w es el resultado de esa operación. Para redondear el resultado utilizamos la función round, indicamos que queremos redondear y después de la coma indicamos a que decimal queremos redondearlo.
w= (365/12)*14.7
wround= round(w,2)
print(wround)
print("\n")

#EJERCICIO 3.- Para que el usuario pueda introducir el texto que quiera utilizaremos la función input.

username= input("Introduce your username: ")
password= input("Introduce your password: ")

if (3 <= len(username) < 10): 
  print("True")
else:
  print("False")

if password == ("PYTHON") or password == ("TOKIO"):
  print("True")
else: 
  print("False")






