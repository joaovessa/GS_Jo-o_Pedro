d = int(input('Quantos desastres você deseja computar? '))
desastres=[]

for i in range (d):
    print(f'\n Cadastro do desastre {i+1} de {d}')
    tipo= input('Qual é o tipo do desastre? ')
    pais= input('Qual pais ocorreu o desastre? ')
    cidade = input('Qual cidade ocorreu o desastre? ')
    bairro = input('Qual bairro ocorreu o desastre? ')
    rua = input('Qual rua ocorreu o desastre? ')
    pA = int(input('Quantas pessoas foram afetadas no desastre? '))
    pC= int(input('Quantas pessoas afetadas são crianças '))
    pAd = int(input('Quantas pessoas afetadas são adultos '))
    pI = int(input('Quantas pessoas afetadas são idosos '))
    pCD = int(input('Quantas pessoas afetadas tem mobilidade reduzida '))
    pF =int(input('Quantas pessoas afetadas foram feridas '))
    while pA!= pC+pAd+pF+pCD+pI:
        print('Numero de pessoas afetadas não condiz com as especificações, Tente novamente ')
        pC = int(input('Quantas pessoas afetadas são crianças '))
        pAd = int(input('Quantas pessoas afetadas são adultos '))
        pI = int(input('Quantas pessoas afetadas são idosos '))
        pCD = int(input('Quantas pessoas afetadas tem mobilidade reduzida '))
        pF = int(input('Quantas pessoas afetadas foram feridas '))


