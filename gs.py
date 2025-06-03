d = int(input('Quantos desastres você deseja computar? '))

desastres = []
total_afetados = 0
total_criancas = 0
total_adultos = 0
total_idosos = 0
total_com_deficiencia = 0
total_feridos = 0

maior_afetados = 0
desastre_mais_grave = None

for i in range(d):
    print(f'\nCadastro do desastre {i+1} de {d}')
    tipo = input('Qual é o tipo do desastre? ')
    pais = input('Qual país ocorreu o desastre? ')
    cidade = input('Qual cidade ocorreu o desastre? ')
    bairro = input('Qual bairro ocorreu o desastre? ')
    rua = input('Qual rua ocorreu o desastre? ')
    pA = int(input('Quantas pessoas foram afetadas no desastre? '))
    pC = int(input('Quantas pessoas afetadas são crianças? '))
    pAd = int(input('Quantas pessoas afetadas são adultos? '))
    pI = int(input('Quantas pessoas afetadas são idosos? '))
    pCD = int(input('Quantas pessoas afetadas têm mobilidade reduzida? '))
    pF = int(input('Quantas pessoas afetadas foram feridas? '))

    while pA != (pC + pAd + pI + pCD + pF):
        print('Número de pessoas afetadas não condiz com as especificações. Tente novamente.')
        pC = int(input('Quantas pessoas afetadas são crianças? '))
        pAd = int(input('Quantas pessoas afetadas são adultos? '))
        pI = int(input('Quantas pessoas afetadas são idosos? '))
        pCD = int(input('Quantas pessoas afetadas têm mobilidade reduzida? '))
        pF = int(input('Quantas pessoas afetadas foram feridas? '))

    local = [pais, cidade, bairro, rua]
    categorias = [pC, pAd, pI, pCD, pF]

    desastres.append({
        "tipo": tipo,
        "local": local,
        "afetados": pA,
        "categorias": categorias
    })


    total_afetados += pA
    total_criancas += pC
    total_adultos += pAd
    total_idosos += pI
    total_com_deficiencia += pCD
    total_feridos += pF

    if pA > maior_afetados:
        maior_afetados = pA
        desastre_mais_grave = {
            "tipo": tipo,
            "local": local,
            "afetados": pA
        }

categorias_totais = {
    "Crianças": total_criancas,
    "Adultos": total_adultos,
    "Idosos": total_idosos,
    "Com mobilidade reduzida": total_com_deficiencia,
    "Feridos": total_feridos
}
categoria_mais_afetada = max(categorias_totais, key=categorias_totais.get)

print('\n--- RELATÓRIO FINAL ---')
print(f'Total de Desastres Registrados: {d}')
print(f'Total Geral de Pessoas Afetadas: {total_afetados}')
print('Total de Pessoas por Categoria:')
print(f' - Crianças: {total_criancas}')
print(f' - Adultos: {total_adultos}')
print(f' - Idosos: {total_idosos}')
print(f' - Com mobilidade reduzida: {total_com_deficiencia}')
print(f' - Feridos: {total_feridos}')
print(f'Categoria mais afetada no geral: {categoria_mais_afetada} ({categorias_totais[categoria_mais_afetada]} pessoas)')
print('\nDesastre com maior número de afetados:')
print(f' - Tipo: {desastre_mais_grave["tipo"]}')
print(f' - Total de afetados: {desastre_mais_grave["afetados"]}')
print(f' - Local: Rua {desastre_mais_grave["local"][3]}, Bairro {desastre_mais_grave["local"][2]}, Cidade {desastre_mais_grave["local"][1]}, País {desastre_mais_grave["local"][0]}')
