#arreglar de forma ascendente
numbers = []
print("Bienvenido, vamos a ordenar números en forma ascendente :D")
print("Escribe tu número e ingresa YA cuando hayas acabado:")
while True:
    try:
        num = int(input("Número: "))
        
        numbers.append(num)
    except ValueError:
        break

print("Lista de números ingresados:", numbers)
ordered = False
while not ordered:
    changes = 0
    for i in range(len(numbers)-1):
          if numbers[i] > numbers[i+1]:
              aux = numbers[i]
              numbers[i] = numbers[i+1]
              numbers[i+1] = aux
              changes += 1
    if changes == 0:
        ordered = True
print("Los números ordenados son: ", numbers)




