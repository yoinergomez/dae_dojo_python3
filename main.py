class dojo:

    def __init__(self, x, y, s):
        self.rango = range(x, y, s)


    def sum(self):
        suma = 0
        for i in self.rango:
            suma += i #Sumando valores
        print(suma)
        return suma


print("Ingrese menor:")
menor = int(input())

print("Ingrese mayor:")
mayor = int(input())

print("Ingrese salto:")
salto = int(input())

#rango = range(menor, mayor)
#print("La suma es:", sum(rango))

calcular = dojo(menor, mayor, salto)

calcular.sum()
