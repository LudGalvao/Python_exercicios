a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))

if a == 0:
  print("A equação não é do segundo grau.")
else:
  delta = b**2 - 4*a*c

  if delta < 0:
    print("A equação não possui raízes reais.")
 
  elif delta == 0:
    x = -b / (2*a)
    print("A equação possui apenas uma raiz real:", x)

  else:
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    print("A equação possui duas raízes reais:", x1, "e", x2)