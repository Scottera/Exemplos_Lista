pessoas = [] #Exemplo de lista vazia
numeros = list() #Outro exemplo de lista vazia

pessoas = ['Lucas', 'Renan', 'Scotti', 'Rios']
numeros = [1,2,3,4,5,6]

print(pessoas[1])
print('----------')
print(pessoas)
print('----------')

#Cria um range do tamanho da lista, e sua a variável i como índice (posição) de cada elemento da lista
for i in range(len(pessoas)):
    print(pessoas[i])
    print('----------')


#Percorre a lista de pessoas, atribuindo à variável p cada elemento na lista
for p in pessoas:
    print(p)
    print('----------')

#Traz a posição e o nome
for i, p in enumerate(pessoas):
    print(f'Nome: {p} na posição {i}')


print('----------')
#Saber tamanho da lista
print(len(numeros))

#Atribuindo valores a lista
pessoas = []

for i in range(5):
    nome = input(f'Informe o nome da pessoas {i}: ')
    pessoas.append(nome)
    print(f'Tamanho atual da lista: {len(pessoas)}')

#Obtém a posição de um item na lista
pos_maria = pessoas.index('Maria')
print(f'Maria está na posição {pos_maria}')



