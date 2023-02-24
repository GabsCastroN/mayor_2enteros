# input

X = int(input("X: "))

Y = int(input("Y: "))

# processing
if X == Y:
    # output
    print("los numeros son iguales")
else:
    if X > Y:
        mayor = X
    else:
            mayor = Y
    print("el mayor entre: " + str(X) + " y " + str(Y) + " es " + str(mayor))