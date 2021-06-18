import numpy as np

c_mat_1 = int(input("Ingrese el tamaño de columnas de la matriz 1: "))
f_mat_1 = int(input("Ingrese el numero de filas de la matriz 1: "))

c_mat_2 = int(input("Ingrese el tamaño de columnas de la matriz 2: "))
f_mat_2 = int(input("Ingrese el numero de filas de la matriz 2: "))



while(f_mat_1 != c_mat_2 ):
  

  print ("Datos Ingresado erroneos\n Vuelva a ingresar\n")

  f_mat_1 = int(input("Ingrese el numero de filas de la matriz 1: "))
  c_mat_2 = int(input("Ingrese el tamaño de columnas de la matriz 2: "))
  if(f_mat_1 == c_mat_2):
    break

Mat1 = np.zeros((c_mat_1,f_mat_1)) #aqui columnas (columnas, filas)
Mat2 = np.zeros((c_mat_2,f_mat_2))

Resul = np.zeros((c_mat_2,f_mat_1))


print ("\nMatriz 1\n")
for i in range(f_mat_1):
    for j in range(c_mat_1):
        Mat1[i][j] = int(input("Ingrese los digitos matriz 1: "))
        
    
print ("\nMatriz 2\n")
for i in range(f_mat_2):
    for j in range(c_mat_2):
        Mat2[i][j] = int(input("Ingrese los digitos matriz 2: "))
    
print ("\nMultiplicacion de las matrices: \n",np.dot(Mat1,Mat2))