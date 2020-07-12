
from datetime import datetime

dibairros = {"santana": 3.00, "barreto": 3.00, 'ilha da conceição': 3.00,
             'engenhoca': 3.00,
             'bairro de fatima': 5.00,
             'centro': 5.00,
             'sao lourenço': 5.00,
             "ponta d'areia": 5.00,
             'neves': 5.00,
             'venda da cruz': 5.00,
             'tenente jardim': 5.00,
             'icarai': 5.00,
             'covanca': 5.00,
             'morro do estado': 5.00,
             'cubango': 5.00,
             'boa viagem': 5.00,
             'sao domingos': 5.00,
             'fonseca': 5.00,
             'inga': 5.00,
             'pe pequeno': 6.00,
             'vila lage': 6.00,
             'porto velho': 6.00,
             'morro do castro': 6.00,
             'pita': 6.00,
             'santa rosa': 6.00,
             'viçoso jardim': 6.00,
             'barro vermelho': 6.00,
             'gragoata': 6.00,
             'vital brazil': 7.00,
             'porto da madama': 7.00,
             'paraiso': 7.00,
             'baldeador': 7.00,
             'sao francisco': 7.00,
             'viradouro': 7.00,
             'ititioca': 7.00,
             'santa catarina': 7.00,
             'mangueira': 7.00,
             'caramujo': 7.00,
             'patronato': 7.00,
             'parada quarenta': 7.00,
             'engenho pequeno': 7.00,
             'gradim': 7.00,
             'lindo parque': 8.00,
             'porto novo': 8.00,
             'charitas': 8.00,
             'camarao': 8.00,
             'largo da batalha': 9.00,
             'zumbi': 9.00,
             'santa barbara': 9.00,
             'maceio': 9.00,
             'centro de sg': 7.00,
             'rocha': 8.00,
             'jurujuba': 9.00,
             'badu': 9.00,
             'sape': 10.00,
             'galo branco': 10.00,
             'porto da pedra': 10.00,
             'estrela do norte': 10.00,
             'boa vista': 10.00,
             'brasilandia': 9.00,
             'cafuba': 10.00,
             'vila progresso': 10.00,
             'antonina': 9.00,
             'cantagalo': 10.00,
             'vila iara': 10.00,
             'boaçu': 9.00,
             'rosane': 10.00,
             'tribobo': 10.00,
             'ze garoto': 8.00,
             'maria paula': 10.00,
             'porto do rosa': 10.00,
             'itauna': 10.00,
             'itaipu': 10.00,
             'camboinhas': 10.00,
             'santo antonio': 10.00,
             'alcantara': 10.00,
             'matapaca': 10.00,
             'mutuaguaçu': 10.00,
             'mutua': 10.00,
             'colubande': 10.00,
             'mutuapira': 10.00,
             'recanto das acacias': 10.00,
             'luiz caçador': 10.00,
             'vila tres': 10.00,
             'mutondo': 10.00,
             'piratininga': 10.00,
             'cruzeiro do sul': 10.00,
             'fazenda dos mineiros': 10.00,
             'almerinda': 10.00,
             'nova cidade': 10.00,
             '0': 0.0}

parada = False
total = 0
while not parada:
    bairro = input("Qual bairro : ")
    try:
        valor = dibairros[bairro]
    except:
        print("Bairro invalido")
        continue
    total += valor
    if bairro == "0":
        parada = True

hoje = datetime.now()

print("TOTAL A PAGAR R${}".format(total))
print(hoje.strftime('%d-%b-%y'))


