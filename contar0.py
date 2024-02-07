numeros = int(input("Cuantos números quiere ingresar?: "))
arr = []
ceros = 0
for i in range(numeros):
  i = int(input("Inserte un número: "))
  if(i == 0):
    ceros += 1
  arr.append(i)
print("Los numeros son: ", arr)
print(f"Hay {ceros} ceros")