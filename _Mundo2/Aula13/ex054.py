from datetime import datetime

birthyear = []
age = []
actualyear = datetime.now().year
maior = 0
minor = 0
for i in range(1, 8):
    birthyear.append(int(input(f"Em que ano nasceu a {i} pessoa ? :")))
    age.append(actualyear - birthyear[i - 1])
    if age[i - 1] >= 18:
        maior += 1
    else:
        minor += 1
print(f"Ao todo tivemos {maior} pessoas maiores de idade")
print(f"E tambem tivemos {minor} pessoas menores de idade")
