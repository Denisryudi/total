qtde_pessoas = int(input('Digite a quantidade de pessoas: '))
quarto = []

for i in range(qtde_pessoas):
    cpf = int(input('Digite o CPF: '))
    nome = input('Digite o nome: ')
    hospede = [cpf, nome]
    quarto.append(hospede)
print(quarto)


