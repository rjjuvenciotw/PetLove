# Dicionários para armazenar dados:
usuarios = {}
clientes = {}
pets = {}
servicos = {}
agendamentos = {}

# Códigos de cores ANSI.
RESET = "\033[0m"
BOLD = "\033[01m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"

# 1.0 - Função para exibir o menu principal.
def menu():
    while True:
        print(f"\n{BOLD}{CYAN}Menu Principal{RESET}")
        print(f"{YELLOW}1.{RESET} Cadastros")
        print(f"{YELLOW}2.{RESET} Agendamentos")
        print(f"{YELLOW}3.{RESET} Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_cadastros()
        elif opcao == "2":
            menu_agendamentos()
        elif opcao == "3":
            print(f"{GREEN}Saindo...{RESET}")
            break
        else:
            print(f"{RED}Opção inválida!{RESET}")

# 1.1 - Função para exibir o menu de cadastros.
def menu_cadastros():
    while True:
        print(f"\n{BOLD}{CYAN}Menu de Cadastros{RESET}")
        print(f"{YELLOW}1.{RESET} Usuários")
        print(f"{YELLOW}2.{RESET} Clientes")
        print(f"{YELLOW}3.{RESET} Pets")
        print(f"{YELLOW}4.{RESET} Serviços")
        print(f"{YELLOW}5.{RESET} Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_opcoes(usuarios, "Usuário")
        elif opcao == "2":
            menu_opcoes(clientes, "Cliente")
        elif opcao == "3":
            menu_opcoes(pets, "Pet")
        elif opcao == "4":
            menu_opcoes(servicos, "Serviço")
        elif opcao == "5":
            break
        else:
            print(f"{RED}Opção inválida!{RESET}")

# 1.2 - Função para exibir o menu de opções de cadastro.
def menu_opcoes(dicionario, tipo):
    while True:
        print(f"\n{BOLD}{CYAN}{tipo}s{RESET}")
        print(f"{YELLOW}1.{RESET} Cadastrar")
        print(f"{YELLOW}2.{RESET} Atualizar")
        print(f"{YELLOW}3.{RESET} Apagar")
        print(f"{YELLOW}4.{RESET} Consultar")
        print(f"{YELLOW}5.{RESET} Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar(dicionario, tipo)
        elif opcao == "2":
            atualizar(dicionario, tipo)
        elif opcao == "3":
            apagar(dicionario, tipo)
        elif opcao == "4":
            consultar(dicionario, tipo)
        elif opcao == "5":
            break
        else:
            print(f"{RED}Opção inválida!{RESET}")

# 1.3 - Função para cadastrar um novo usuário, cliente, pet ou serviço.
def cadastrar(dicionario, tipo):
    print(f"\n{BOLD}{GREEN}Cadastrar {tipo}{RESET}")
    id_ = input("ID: ")
    if id_ in dicionario:
        print(f"{RED}{tipo} já cadastrado!{RESET}")
    else:
        nome = input("Nome: ")
        if tipo == "Pet":
            print("\nEscolha o tipo do pet:")
            print(f"{YELLOW}1.{RESET} Cachorro")
            print(f"{YELLOW}2.{RESET} Gato")
            print(f"{YELLOW}3.{RESET} Pássaro")
            opcao_tipo = input("Digite o número correspondente ao tipo: ")
            if opcao_tipo == "1":
                tipo_pet = "Cachorro"
            elif opcao_tipo == "2":
                tipo_pet = "Gato"
            elif opcao_tipo == "3":
                tipo_pet = "Pássaro"
            else:
                print(f"{RED}Opção inválida! O pet será cadastrado como 'Desconhecido'.{RESET}")
                tipo_pet = "Desconhecido"
            dicionario[id_] = {"nome": nome, "tipo": tipo_pet}
        elif tipo == "Serviço":
            descricao = input("Descrição do Serviço: ")
            while True:
                try:
                    preco = float(input("Preço (em R$): ").replace(',', '.'))
                    break
                except ValueError:
                    print(f"{RED}Preço inválido! Por favor, insira um número válido.{RESET}")
            dicionario[id_] = {"nome": nome, "descrição": descricao, "preço": preco}
        else:
            dicionario[id_] = {"nome": nome}
        print(f"{GREEN}{tipo} cadastrado com sucesso!{RESET}")

# 2.0 - Função para atualizar um usuário, cliente, pet ou serviço.
def atualizar(dicionario, tipo):
    print(f"\n{BOLD}{YELLOW}Atualizar {tipo}{RESET}")
    id_ = input("ID: ")
    if id_ not in dicionario:
        print(f"{RED}{tipo} não encontrado!{RESET}")
    else:
        nome = input("Novo Nome (Deixe em branco para manter o atual): ") or dicionario[id_]["nome"]
        if tipo == "Pet":
            print("\nEscolha o novo tipo do pet (ou deixe em branco para manter atual):")
            print(f"{YELLOW}1.{RESET} Cachorro")
            print(f"{YELLOW}2.{RESET} Gato")
            print(f"{YELLOW}3.{RESET} Pássaro")
            opcao_tipo = input("Digite o número correspondente ao tipo: ") or ""
            if opcao_tipo == "1":
                tipo_pet = "Cachorro"
            elif opcao_tipo == "2":
                tipo_pet = "Gato"
            elif opcao_tipo == "3":
                tipo_pet = "Pássaro"
            else:
                tipo_pet = dicionario[id_]["tipo"]
            dicionario[id_]["nome"] = nome
            dicionario[id_]["tipo"] = tipo_pet
        elif tipo == "Serviço":
            descricao = input("Nova Descrição (Deixe em branco para manter atual): ") or dicionario[id_]["descrição"]
            while True:
                preco_input = input(f"Novo Preço (Atual: R$ {dicionario[id_]['preço']:.2f}): ").replace(',', '.')
                if not preco_input:
                    preco = dicionario[id_]['preço']
                    break
                try:
                    preco = float(preco_input)
                    break
                except ValueError:
                    print(f"{RED}Preço inválido! Por favor, insira um número válido.{RESET}")
            dicionario[id_]["nome"] = nome
            dicionario[id_]["descrição"] = descricao
            dicionario[id_]["preço"] = preco
        else:
            dicionario[id_]["nome"] = nome
        print(f"{GREEN}{tipo} atualizado com sucesso!{RESET}")

# 2.1 - Função para apagar um usuário, cliente, pet ou serviço.
def apagar(dicionario, tipo):
    print(f"\n{BOLD}{RED}Apagar {tipo}{RESET}")
    id_ = input("ID: ")
    if id_ in dicionario:
        del dicionario[id_]
        print(f"{GREEN}{tipo} apagado com sucesso!{RESET}")
    else:
        print(f"{RED}{tipo} não encontrado!{RESET}")

# 2.2 - Função para consultar usuários, clientes, pets ou serviços.
def consultar(dicionario, tipo):
    print(f"\n{BOLD}{BLUE}Consultar {tipo}s{RESET}")
    if not dicionario:
        print(f"{YELLOW}Nenhum {tipo} cadastrado.{RESET}")
    else:
        if tipo == "Pet":
            print(f"{BOLD}{'ID':<10} {'Nome':<20} {'Tipo':<15}{RESET}")
            for id_, dados in dicionario.items():
                print(f"{id_:<10} {dados['nome']:<20} {dados['tipo']:<15}")
        elif tipo == "Serviço":
            print(f"{BOLD}{'ID':<10} {'Nome':<20} {'Descrição':<30} {'Preço':<10}{RESET}")
            for id_, dados in dicionario.items():
                print(f"{id_:<10} {dados['nome']:<20} {dados['descrição']:<30} R$ {dados['preço']:<10.2f}")
        else:
            print(f"{BOLD}{'ID':<10} {'Nome':<20}{RESET}")
            for id_, dados in dicionario.items():
                print(f"{id_:<10} {dados['nome']:<20}")

# 3.0 - Função para exibir o menu de agendamentos.
def menu_agendamentos():
    while True:
        print(f"\n{BOLD}{CYAN}Menu de Agendamentos{RESET}")
        print(f"{YELLOW}1.{RESET} Agendar Serviço")
        print(f"{YELLOW}2.{RESET} Visualizar Agendamentos")
        print(f"{YELLOW}3.{RESET} Cancelar Agendamento")
        print(f"{YELLOW}4.{RESET} Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            agendar_servico()
        elif opcao == "2":
            consultar_agendamentos()
        elif opcao == "3":
            cancelar_agendamento()
        elif opcao == "4":
            break
        else:
            print(f"{RED}Opção inválida!{RESET}")

# 3.1 - Função para agendar um serviço.
def agendar_servico():
    print(f"\n{BOLD}{GREEN}Agendar Serviço{RESET}")
    id_agendamento = input("ID do Agendamento: ")
    if id_agendamento in agendamentos:
        print(f"{RED}Agendamento com este ID já existe!{RESET}")
        return
    id_cliente = input("ID do Cliente: ")
    if id_cliente not in clientes:
        print(f"{RED}Cliente não encontrado!{RESET}")
        return
    id_pet = input("ID do Pet: ")
    if id_pet not in pets:
        print(f"{RED}Pet não encontrado!{RESET}")
        return
    id_servico = input("ID do Serviço: ")
    if id_servico not in servicos:
        print(f"{RED}Serviço não encontrado!{RESET}")
        return
    data = input("Data do Agendamento (DD/MM/AAAA): ")
    hora = input("Hora do Agendamento (HH:MM): ")

    agendamentos[id_agendamento] = {
        "cliente": clientes[id_cliente]["nome"],
        "pet": pets[id_pet]["nome"],
        "serviço": servicos[id_servico]["nome"],
        "data": data,
        "hora": hora
    }
    print(f"{GREEN}Serviço agendado com sucesso para {data} às {hora}!{RESET}")

# 3.2 - Função para consultar os agendamentos.
def consultar_agendamentos():
    print(f"\n{BOLD}{BLUE}Agendamentos{RESET}")
    if not agendamentos:
        print(f"{YELLOW}Nenhum agendamento encontrado.{RESET}")
    else:
        print(f"{BOLD}{'ID':<10} {'Cliente':<20} {'Pet':<20} {'Serviço':<20} {'Data':<12} {'Hora':<8}{RESET}")
        for id_, dados in agendamentos.items():
            print(f"{id_:<10} {dados['cliente']:<20} {dados['pet']:<20} {dados['serviço']:<20} {dados['data']:<12} {dados['hora']:<8}")

# 3.3 - Função para cancelar um agendamento.
def cancelar_agendamento():
    print(f"\n{BOLD}{RED}Cancelar Agendamento{RESET}")
    id_agendamento = input("ID do Agendamento: ")
    if id_agendamento in agendamentos:
        del agendamentos[id_agendamento]
        print(f"{GREEN}Agendamento cancelado com sucesso!{RESET}")
    else:
        print(f"{RED}Agendamento não encontrado!{RESET}")

# 0.0 Função para iniciar o programa:
menu()