import math as m

base = float(input("\nDigite base: "))
altura = float(input("\nDigite altura: "))
perimetro = 2*(base+altura)
area = base*altura
diagonal = m.sqrt(base**2+altura**2)
print(f"\n Perímetro: {perimetro}")
print(f"\n Área: {area}")
print(f"\n Diagonal: {diagonal:.2f}")
print("\n")