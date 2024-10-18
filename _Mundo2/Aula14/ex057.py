def dadosInvalidos():
    print("Dados inválidos, por favor informe seu sexo: ")


def sexoRegistrado(g):
    print(f"Sexo {g} registrado com sucesso")


gender = "M"
while True:
    gender = str(input("Informe o seu sexo: [M/F] : "))
    gender = gender.upper()
    if gender in ["M", "F"]:
        sexoRegistrado(gender)
        break
    else:
        dadosInvalidos()
