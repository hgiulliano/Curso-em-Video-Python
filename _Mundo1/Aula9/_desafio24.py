city = input('Digite o nome da sua cidade: ').strip()
city = city.capitalize()#só posso usar em string, quando transformo em array já não da
city = city.split()
print(city)
print(f'A sua cidade começa com Santo no nome? : {'Santo' in city[0]}')