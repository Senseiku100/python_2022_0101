lado=0
alto=0
perimetro=0

print("Bienvenido a la calculadora")
print()
print("Ingrese el dato del lado:")
lado = input()

print("Ingrese el dato del alto")
alto = input()

perimetro = int(lado) * int(alto)
print(f"El perimetro es = {perimetro}")