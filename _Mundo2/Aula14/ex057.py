def dadosInvalidos():
    print("Dados inválidos, por favor informe seu sexo: ")


def sexoRegistrado():
    print(f"Sexo {gender} registrado com sucesso")


gender = "M"
while True:
    gender = str(input("Informe o seu sexo: [M/F] : "))
    gender = gender.upper()
    if gender in ["M", "F"]:
        sexoRegistrado()
        break
    else:
        dadosInvalidos()
