import json
import os

ARQUIVO = 'mymoney.json'

def carregar_dados():
    #Carrega os dados do arquivo JSON ou cria uma estrutura vazia se não existir.
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'r') as f:            
            return json.load(f)
    return {"receitas": [], "despesas": []}

def salvar_dados(dados):
    with open(ARQUIVO, 'w') as f:
        json.dump(dados, f, indent=4)

def adicionar_registro(tipo, dados):
    descricao = input(f"Digite a descrição da {tipo}: ")
    try:
        # Adicionado o 'f' no input e replace para aceitar vírgula
        valor_str = input(f"Digite o valor da {tipo} (ex: 150.00): ").replace(',', '.')
        valor = float(valor_str)
    except ValueError:
        print("Valor inválido! Por favor, digite apenas números.")
        return
    
    # Ajuste para garantir que a chave certa do dicionário seja acessada
    chave = "receitas" if tipo == "receita" else "despesas"
    dados[chave].append({"descricao": descricao, "valor": valor})
    
    salvar_dados(dados)
    print(f"\n{tipo.capitalize()} adicionada com sucesso!")

def mostrar_resumo(dados):
    total_receitas = sum(item["valor"] for item in dados["receitas"])
    total_despesas = sum(item["valor"] for item in dados["despesas"])
    saldo = total_receitas - total_despesas
    
    # Adicionado os prints para exibir o resultado para o usuário
    print("\n--- Resumo Financeiro ---")
    print(f"Total de Receitas: R$ {total_receitas:.2f}")
    print(f"Total de Despesas: R$ {total_despesas:.2f}")
    print(f"Saldo Atual: R$ {saldo:.2f}")
    print("-------------------------")

def listar_registros(dados):
    """Nova função para exibir o extrato detalhado."""
    print("\n--- Extrato de Registros ---")
    
    print("RECEITAS:")
    if not dados["receitas"]:
        print("  Nenhuma receita registrada.")
    else:
        for i, item in enumerate(dados["receitas"], 1):
            print(f"  {i}. {item['descricao']} - R$ {item['valor']:.2f}")

    print("\nDESPESAS:")
    if not dados["despesas"]:
        print("  Nenhuma despesa registrada.")
    else:
        for i, item in enumerate(dados["despesas"], 1):
            print(f"  {i}. {item['descricao']} - R$ {item['valor']:.2f}")
    print("----------------------------")

def menu_principal():
    dados = carregar_dados()

    while True:
        # Criação de uma interface
        print("\n=== MyMoney - Menu Principal ===")
        print("1. Adicionar Receita")
        print("2. Adicionar Despesa")
        print("3. Mostrar Resumo Financeiro")
        print("4. Listar Extrato")
        print("5. Sair")
        print("================================")

        escolha = input("Escolha uma opção (1-5): ")

        if escolha == '1':
            adicionar_registro("receita", dados)
        elif escolha == '2':
            adicionar_registro("despesa", dados)
        elif escolha == '3':
            mostrar_resumo(dados)
        elif escolha == '4':
            listar_registros(dados)
        elif escolha == '5':
            print("\nSalvando dados e saindo... Até logo!")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    menu_principal()