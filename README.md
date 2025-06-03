
# Cadastro de Desastres Naturais

##  Como Usar

1. **Abra o terminal.**
2. Informe quantos desastres você deseja cadastrar.
3. Para cada desastre, insira:
   - Tipo de desastre (ex: enchente, deslizamento, incêndio etc.)
   - País, cidade, bairro e rua onde ocorreu
   - Número total de pessoas afetadas
   - Quantas são crianças, adultos, idosos, com mobilidade reduzida e feridos

4. O programa verificará se a soma das categorias corresponde ao número total de afetados. Caso não bata, ele pedirá para inserir novamente.
5. Ao final do cadastro, será exibido um **relatório completo** no terminal.

---

##  Exemplo de Entrada

```
Quantos desastres você deseja computar? 2

Cadastro do desastre 1 de 2
Qual é o tipo do desastre? Enchente
Qual país ocorreu o desastre? Brasil
Qual cidade ocorreu o desastre? São Paulo
Qual bairro ocorreu o desastre? Mooca
Qual rua ocorreu o desastre? Rua do Orvalho
Quantas pessoas foram afetadas no desastre? 50
Quantas pessoas afetadas são crianças? 10
Quantas pessoas afetadas são adultos? 20
Quantas pessoas afetadas são idosos? 10
Quantas pessoas afetadas têm mobilidade reduzida? 5
Quantas pessoas afetadas foram feridas? 5
```

---

##  Relatório Final Gerado (exemplo)

```
--- RELATÓRIO FINAL ---
Total de Desastres Registrados: 2
Total Geral de Pessoas Afetadas: 120
Total de Pessoas por Categoria:
 - Crianças: 30
 - Adultos: 50
 - Idosos: 20
 - Com mobilidade reduzida: 10
 - Feridos: 10
Categoria mais afetada no geral: Adultos (50 pessoas)

Desastre com maior número de afetados:
 - Tipo: Deslizamento
 - Total de afetados: 70
 - Local: Rua da Esperança, Bairro Centro, Cidade Petrópolis, País Brasil
```