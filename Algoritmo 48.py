import math as m

sm = float(input("\nEntre com o salário mínimo: "))
qtidade = float(input("\nEntre com a quantidade em quilowatt: "))
preco = sm/700
vp = preco*qtidade
vd = vp*0.9
print(f"\n Preço do quilowatt: {preco}\n Valor a ser pago: {vp}\n Valor com desconto: {vd}")
print("\n")