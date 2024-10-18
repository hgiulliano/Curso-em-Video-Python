print("=" * 20)
print("10 TERMOS DE UMA P.A")
print("=" * 20)
firstterm = int(input("Digite o primeiro termo da sua P.A : "))
r = int(input("Digite a razão da sua P.A : "))
for n in range(1, 11):
    an = firstterm + (n - 1) * r
    print(an, end=" -> ")
print("Acabou")
