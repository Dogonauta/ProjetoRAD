def listaCrescente(min, max):
   with open('crescente.txt', 'w', encoding='UTF-8') as arquivo:
    for i in range(min, max+1):
        arquivo.write(f'{i};')

listaCrescente(1,100) 

