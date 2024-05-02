def saque(num_saque, lim_saque, val_max, conta_att):
    print(conta_att);
    resposta_saque = float(input("[0] Sair\nSelecione o valor\n=>"));

    print(conta_att);

    while True:
        if resposta_saque == 0:
            print("\nVoltando.");
            break;
        elif resposta_saque > val_max:
            print("\nO valor maximo eh R$ 500.00. Tente novamente.");
            break;
        elif resposta_saque < 0:
            print("\nNao eh possivel sacar R$ 0.00 ou menos. Tente novamente");
            break;
        elif num_saque >= lim_saque:
            print("\nEh possivel sacar apenas 3 vezes por dia. Tente novamente amanha.");

            break;
        elif num_saque > conta_att['saldo']:
            print("\nNao eh possivel sacar uma quantidade maior que o seu saldo da conta. Tente novamente");
            break;
        else:
            num_saque += 1;

            print(f"\nR$ {resposta_saque:.2f} sacados.");
            conta_att['saldo'] -= resposta_saque;
            conta_att['print_extrato'] += f"Saque: R$ {resposta_saque:.2f}\n";

            print(conta_att);

            break;

def deposito(conta_att):
    print(conta_att);
    resposta_deposito = float(input("[0] Sair\nSelecione o valor\n=>"));

    while True:
        if resposta_deposito == 0:
            print("\nVoltando.");
            break;
        elif resposta_deposito < 0:
            print("\nNao eh possivel depositar R$ 0.00 ou menos. Tente novamente.");
        else:
            print(f"\nR$ {resposta_deposito:.2f} depositados.");
            conta_att['saldo'] += resposta_deposito;
            conta_att['print_extrato'] += f"Deposito: R$ {resposta_deposito:.2f}\n";

            print(conta_att);

            break;

def extrato(conta_att):
    print(conta_att['print_extrato']);
    print(conta_att);
    if conta_att['print_extrato'] != "":
        print(conta_att['print_extrato']);
        print(f"\nSaldo: R$ {conta_att['saldo']:.2f}\n");
    else:
        print("Movimentacoes ainda nao foram realizadas. Tente novamente mais tarde.\n");

def cadastrar_usuario(clientes, lista_clientes):
    print("=-================================-=")
    print("\nBem-vindo(a) ao cadastro de usuario!");
    print("\nDigite suas informacoes a seguir");

    while True:
        resposta_cpf = int(input("\nCPF: "));

        if len(str(abs(int(resposta_cpf)))) != 11:
            print("\nO CPF deve conter 11 numeros. Tente novamente.");
        elif str(resposta_cpf).isalpha():
            print("\nO CPF nao pode conter caracteres. Tente novamente.");
        elif resposta_cpf in clientes:
            print("\nEste CPF ja foi cadastrado. Tente novamente.");
        else:
            print(f"CPF selecionado: {resposta_cpf}\n");
            clientes.append(resposta_cpf);
            break;

    while True:
        resposta_nome = input("\nNome: ");

        if not resposta_nome.isdigit():
            print(f"Nome selecionado: {resposta_nome}\n");
            clientes.append(resposta_nome);
            break;
        else:
            print("O nome nao pode conter numeros. Tente novamente.\n");

    while True:
        resposta_nascimento = input("\nData de nascimento (dd/mm/aaaa): ");
        
        if "/" not in resposta_nascimento:
            print("Resposta invalida! O formato da data eh (dd/mm/aaaa). Tente novamente.\n");
        elif resposta_nascimento.isalpha() and not "/":
            print("A data nao pode conter caracteres, alem da '/'. Tente novamente.\n");
        else:
            print(f"Data de nascimento selecionada: {resposta_nascimento}\n");
            clientes.append(resposta_nascimento);
            break;
    
    logradouro = "Rua {0}, {1} - {2}/{3}";
    print("\n[1] Sair\nEndereco- ");
    #nome do endereco
    while True:
        resposta_endereco_nome = input("\nRua: ");

        if not resposta_endereco_nome.isdigit():
            break;
        else:
            print("\nO nome da rua nao pode conter numeros. Tente novamente.");
    #numero do endereco
    while True:
        resposta_endereco_numero = input("\nNumero: ");

        if not resposta_endereco_numero.isalpha():
            break;
        else:
            print("\nO numero do endereco nao pode conter caracteres. Tente novamente.");
    #cidade do endereco
    while True:
        resposta_endereco_cidade = input("\nCidade: ");

        if resposta_endereco_cidade.isdigit():
            print("\nO nome da cidade nao pode conter numeros. Tente novamente.");
        else:
            break;
    #sigla do endereco
    while True:
        resposta_endereco_sigla = input("\nSigla: ");

        if len(resposta_endereco_sigla) > 2:
            print("\nA sigla nao pode ter mais que 2 caracteres. Tente novamente.");
        elif resposta_endereco_sigla.isdigit():
            print("\nA sigla nao pode conter numeros. Tente novamente.");
        else:
            break;

    resposta_endereco = logradouro.format(resposta_endereco_nome, resposta_endereco_numero, resposta_endereco_cidade, resposta_endereco_sigla);
    clientes.append(resposta_endereco);

    print(f"\n-Usuario criado-\nNome: {resposta_nome}\nData de nascimento: {resposta_nascimento}\nCPF: {resposta_cpf}\nEndereco: {resposta_endereco}\n");

    lista_clientes.append(clientes);

def cadastrar_banco(clientes, lista_clientes, banco, lista_bancos, agc):
    print("=-========================================-=\n");
    print("-Bem-vindo(a) ao cadastro de conta bancaria-");

    while True:
        resposta_cadastro = int(input("\nDigite o seu CPF ou escolha a opcao de sair: "));
        if resposta_cadastro == 1:
            print("\nVoltando.");
            break;
        elif not resposta_cadastro in clientes and len(str(abs(int(resposta_cadastro)))) == 11:
            print("\nCPF nao cadastrado no sistema. Tente novamente.");
        elif not resposta_cadastro in clientes:
            print("\nCPF invalido. Tente novamente.");
        elif str(resposta_cadastro).isalpha():
            print("\nDigite o seu CPF corretamente. Tente novamente.");
        else:
            numero_conta = 0;
            for i in range(len(banco)):
                if i % 3 == 0 or i == 0:
                    if banco[i] > 0:
                        numero_conta = banco[i];
                        numero_conta += 1;
                    else:
                        numero_conta = 0;
                        numero_conta += 1;

            banco.append(numero_conta);
            banco.append(agc);
            banco.append(resposta_cadastro);

            lista_bancos.append(banco);

            print(f"\nCadastro concluido! Conta {numero_conta} do CPF - {resposta_cadastro}");
            print(f"\nAgencia: {agc}\nNumero da conta: {numero_conta}\nUsuario: {resposta_cadastro}\n");
            break;

def entrar_usuario(conta, conjunto_conta, clientes, lista_clientes, banco, lista_bancos, num_saque, lim_saque, val_max):
    while True:
        resposta_entrar = int(input("\n[1] Sair\nDigite seu CPF ou escolha a opcao de sair: "));

        if resposta_entrar == 1:
            print("\nVoltando.");
            break;
        elif not resposta_entrar in clientes and len(str(abs(int(resposta_entrar)))) == 11:
            print("\nEste CPF nao esta cadastrado. Tente novamente.");
        elif str(resposta_entrar).isalpha():
            print("\nDigite o seu CPF corretamente. Tente novamente.");
        elif len(str(abs(int(resposta_entrar)))) != 11:
            print("\nDigite o seu CPF corretamente. Tente novamente.");
        else:
            encontrar_cpf = 0;

            for i in lista_bancos:
                if resposta_entrar == banco[2]:
                    encontrar_cpf += 1;

                    login_final = {'dados': conta['dados'].format(banco[0], banco[2]), 'saldo': 0, 'print_extrato': ""};
                    conjunto_conta.append(login_final);
            
            print(f"\n{encontrar_cpf} contas do banco ligadas ao CPF - {resposta_entrar} encontradas.");

            while True:
                resposta_conta = int(input("\nQual conta deseja entrar?\n=>"));

                if resposta_conta < 0:
                    print("\nOpcao invalida. Tente novamente.");
                else:
                    conta_atual = conjunto_conta[resposta_conta];
                
                    print(f"\n-Conta entrada: {conta_atual['dados']}-");
                    print("\n=-=====================-=");
                    print("\nEscolha a opcao desejada:");

                    while True:
                        resposta_dinheiro = int(input("\n[1] Saque\n[2] Deposito\n[3] Extrato\n[4] Voltar\n=>"));              
                        if resposta_dinheiro == 1:
                            saque(num_saque, lim_saque, val_max, conta_atual);
                            break;
                        elif resposta_dinheiro == 2:
                            deposito(conta_atual);
                            break;
                        elif resposta_dinheiro == 3:
                            extrato(conta_atual);
                            break;
                        elif resposta_dinheiro == 4:
                            break;
                        else:
                            print("\nResposta invalida. Tente novamente.");
                    break;

def main():
    #botar o banco e as conta como classe !!!

    usuarios = [];
    lista_usuarios = [];
    conta_banco = [];
    lista_contas = [];
    login = {'dados': "\nNumero da conta: {0}\nAgencia: 0001\nCPF: {1}", 'saldo': 0, 'print_extrato': ""};
    conjunto_login = [];
    agencia = "0001";

    LIMITE_SAQUE = 3;
    numero_saque = 0;
    valor_max = 500;

    print("=-=============================-=\n");
    print("Bem-vindo(a) ao Sistema bancario!\n");
    while True:
        resposta_menu = int(input("[1] Cadastrar usuario\n[2] Cadastrar conta bancaria\n[3] Entrar\n[4] Sair\n=>"));

        if resposta_menu == 1:
            cadastrar_usuario(usuarios, lista_usuarios);
        elif resposta_menu == 2:
            cadastrar_banco(usuarios, lista_usuarios, conta_banco, lista_contas, agencia);
        elif resposta_menu == 3:
            entrar_usuario(login, conjunto_login, usuarios, lista_usuarios, conta_banco, lista_contas, numero_saque, LIMITE_SAQUE, valor_max);
        elif resposta_menu == 4:
            print("\nSaindo do programa.");
            break;
        else:
            print("Resposta invalida! Tente novamente.\n");

main();