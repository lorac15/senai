num1 = float (input("base maior: "))
num2 = float (input("base menor: "))
num3 = float (input("altura: "))

if num1 == 0: 
    print("apenas numeros acima de 0")

elif num2 == 0: 
    print("apenas numeros acima de 0")

elif num3 == 0: 
    print("apenas numeros acima de 0")

else:
    area = [(num1 + num2) * num3] / 2
    
    print("área do trapézio: ",area)
