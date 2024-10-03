"""
Turma - 93313

Nome completo dos componentes:
1 - Nicolas Roger Araujo Monteiro da Silva
2 - Leonardo Machado
"""

import os 
os.system ("cls||clear")
from dataclasses import dataclass

@dataclass
class Pessoa:
    idade : int
    sexo: str
    salario : float

@dataclass
class Dados_finais:
    lista_final: list

def limpar_terminal():
    os.system("cls || clear")

def calcular_media(a):
    quantidade = len(a)
    if quantidade == 0:
        return 0
    else:
        soma = sum(a)
        media = soma / quantidade
        return media

def criando_arquivo(a,b):
    with open(a,"a") as arquivo_dados:
        for pessoa in b:
            arquivo_dados.write(f"{pessoa.idade},{pessoa.sexo},{pessoa.salario}\n")
    arquivo_dados.close()
    print("\n=== Dados Salvos ===\n")

def criando_arquivo_final(a,b):
    with open(a,"w") as arquivo_dados:
        for dado in b:
            arquivo_dados.write(f"{dado}, \n")
    arquivo_dados.close()
    print("\n=== Dados Salvos ===\n")
    
def lendo_arquivo(a):
    list_dados=[]
    with open(a,"r") as arquivo_origem:
        for linha in arquivo_origem:
            idade, sexo, salario = linha.strip().split(",")
            list_dados.append(Pessoa(idade=int(idade), sexo=str(sexo), salario=float(salario)))
    arquivo_origem.close()
    return list_dados

while True:
    print("""
  Código | Descrição
    1    |  Adicionar pessoa
    2    |  Exibir resultados
    3    |  Sair
    """)
    opcao = int(input("\nInsira a opção desejada:  "))
    match (opcao):
        case 1:
            lista_pessoas = []
            pessoa = Pessoa (
            idade = int(input("Informe a idade: ")),
            sexo = input("Digite 'M' para sexo masculino ou 'F' para sexo feminino: ").upper(),
            salario = float(input("Informe o salário: "))
            )
            lista_pessoas.append(pessoa)
            nome_arquivo = "dados_analise.txt"
            criando_arquivo(nome_arquivo,lista_pessoas)
            limpar_terminal()

        case 2:
            lista_pessoas = []
            nome_arquivo = "dados_analise.txt"
            lista_idade = []
            lista_sexos = []
            lista_salario =[]
            lista_final = []
            lista_pessoas = lendo_arquivo(nome_arquivo)
            quantidade_de_mulheres_com_salario_acima_de_5000 = 0

            for pessoa in (lista_pessoas):
                if pessoa.sexo == "F" and pessoa.salario >= 5000:
                    quantidade_de_mulheres_com_salario_acima_de_5000 +=1
                lista_idade.append(pessoa.idade)
                lista_sexos.append(pessoa.sexo)
                lista_salario.append(pessoa.salario)

            media_salario = calcular_media(lista_salario)
            max_idade = max(lista_idade)
            min_idade = min(lista_idade)

            limpar_terminal()
            print(f"Media salarial do grupo: {media_salario:.2f}")
            print(f"Maior idade do grupo: {max_idade:.2f}")
            print(f"Menor idade do grupo: {min_idade:.2f}")
            print(f"Quantidade de mulheres com salário acima de R$5000,00: {quantidade_de_mulheres_com_salario_acima_de_5000}")
            lista_final.append(media_salario)
            lista_final.append(max_idade)
            lista_final.append(min_idade)
            lista_final.append(quantidade_de_mulheres_com_salario_acima_de_5000)
            nome_arquivo_final = "pesquisa_habitantes.txt"
            criando_arquivo_final(nome_arquivo_final, lista_final)

        case 3:
            print("\nPrograma finalizado.")
            break

        case _:
            print("\nOpção inválida. Por favor, tente novamente.")