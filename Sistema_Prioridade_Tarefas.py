'''
Projeto:        Sistema de Organização de Prioridades em Lista de Tarefas

Universidade:   Universidade Católica de Santos (UNISANTOS)

Cursos:         Ciência da Computação
                Sistemas de Informação

Integrantes:
                Gabriel Coimbra Pajola Bernard
                Gustavo Souza Recouso
                Kauã Asher Ribeiro da Silva
                Kauan Barros Batista
                Pedro Henrique do Nascimento Melo

'''


from datetime import datetime, timedelta
'''
Importando a classe datetime da biblioteca datetime do Python, 
assim permitindo trabalhar com datas e horários.
'''

# Subprograma (procedimento): Salvar Tarefas ---------------------------------------------------------------------------

def salvar_tarefas(lista_tarefas):

    '''
    Realiza o armazenamento das tarefas cadastradas
    no arquivo lista_tarefas.txt, garantindo que os
    dados permaneçam salvos após o encerramento do sistema.
    '''

    with open("lista_tarefas.txt", "w", encoding="utf-8") as arquivo:

        for tarefa in lista_tarefas: 

            linha = (

                tarefa[0] + ";" +
                tarefa[1] + ";" +
                tarefa[2] + ";" +
                tarefa[3] + ";" +
                tarefa[4] + ";" +
                str(tarefa[5]) + ";" + 
                str(tarefa[6]) + "\n"  
            )

            arquivo.write(linha) 


# Subprograma (Função): Carregar Tarefas ------------------------------------------------------------------------------
def carregar_tarefas():

    '''
    Realizar a importação das tarefas previamente salvas
    no arquivo lista_tarefas.txt, efetuando a leitura,
    tratamento e reconstrução da estrutura matricial
    utilizada pelo sistema.
    '''

    lista_tarefas = [] 

    print(" ----------------------------------------------------------------- ")
    print("|       Verificando se existe um arquivo lista_tarefas.txt...     |")
    print("|                                                                 |")

    try: 

        with open("lista_tarefas.txt", "r", encoding="utf-8") as arquivo:

            for linha in arquivo: 

                linha = linha.strip() 

                dados = linha.split(";") 

                
                tarefa = [ 
                    dados[0],
                    dados[1],
                    dados[2],
                    dados[3],
                    dados[4],
                    int(dados[5]), 
                    int(dados[6])  
                ]

                lista_tarefas.append(tarefa) 

        print("|            Arquivo encontrado, extraindo dados...               |")
        print("|                                                                 |")
        print("|             !!!  Importação de dados concluida  !!!             |") 

    except FileNotFoundError: 

        print("|                     Arquivo não encontrado.                     |")
        print("|                                                                 |")
        print("|            !!!  Encerrando Importação de dados  !!!             |")

    print(" ----------------------------------------------------------------- ") 
    input("\n|  Pressione ENTER para continuar...")

    return lista_tarefas 


# Subprograma (Função): Receber Titulo ---------------------------------------------------------------------------------
def receber_titulo():
    
    '''
    Recebe o título da tarefa informado pelo usuário,
    realizando a validação para garantir que o campo
    não fique vazio e respeite o limite máximo de
    50 caracteres.
    '''

    while True:

        titulo = input("\n|  Digite o título [50 caracteres]: ")

        if titulo.strip() == "": 

            print("\n ------------------------------------------------------------------ ")
            print("|             !!!  O título não pode estar vazio  !!!              |")
            print(" ------------------------------------------------------------------ ")
            input("\n|  Pressione ENTER para tentar novamente...")
            continue

        if len(titulo) <= 50: 
            return titulo

        print("\n ------------------------------------------------------------------ ")
        print("|        !!!  O título deve ter no máximo 50 caracteres  !!!       |")
        print(" ------------------------------------------------------------------ ")
        input("\n|  Pressione ENTER para tentar novamente...")


# Subprograma (Função): Receber Descrição ------------------------------------------------------------------------------
def receber_descricao():
    
    '''
    Recebe a descrição da tarefa informada pelo usuário,
    realizando a validação para garantir que o campo
    não fique vazio e respeite o limite máximo de
    200 caracteres.
    '''

    while True:

        descricao = input("\n|  Digite a descrição [200 caracteres]: ")

        if descricao.strip() == "": 

            print("\n ------------------------------------------------------------------ ")
            print("|            !!!  A Descrição não pode estar vazio  !!!            |")
            print(" ------------------------------------------------------------------ ")
            input("\n|  Pressione ENTER para tentar novamente...")
            continue

        if len(descricao) <= 200:
            return descricao

        print("\n ------------------------------------------------------------------ ")
        print("|       !!! A Descrição deve ter no máximo 200 caracteres !!!      |")
        print(" ------------------------------------------------------------------ ")
        input("\n|  Pressione ENTER para tentar novamente...")


# Subprograma (Função): Receber data do inicio -------------------------------------------------------------------------
def receber_data_inicio():
    
    '''
    Recebe a data inicial da tarefa, validando o formato
    informado e permitindo apenas datas entre o dia atual
    e o limite máximo de 1 ano à frente.
    '''

    while True:

        data_inicio = input("\n|  Digite a data de início [DD/MM/AAAA]: ")

        try: 

            
            data_inicio_convertida = datetime.strptime(data_inicio, "%d/%m/%Y")

            limite = datetime.now() + timedelta(days=365) 

            if data_inicio_convertida.date() < datetime.now().date() or data_inicio_convertida.date() > limite.date():

                print("\n ------------------------------------------------------------------ ")
                print("|     !!!  A data deve estar entre hoje até 1 ano à frente !!!     |")
                print(" ------------------------------------------------------------------ ")
                input("\n|  Pressione ENTER para tentar novamente...")
                continue

            return data_inicio, data_inicio_convertida

        except ValueError: 

            print("\n ------------------------------------------------------------------ ")
            print("|     !!!  A data deve estar dentro no formado DD/MM/AAAA  !!!     |")
            print(" ------------------------------------------------------------------ ")
            input("\n|  Pressione ENTER para tentar novamente...")


# Subprograma (Função): Receber data final -----------------------------------------------------------------------------
def receber_data_final(data_inicio_convertida):
    
    '''
    Recebe a data final da tarefa, validando o formato
    informado e verificando se a data está dentro do
    intervalo permitido e posterior à data inicial.
    '''

    while True:

        data_final = input("\n|  Digite a data final [DD/MM/AAAA]: ")

        try:

            data_final_convertida = datetime.strptime(data_final, "%d/%m/%Y")

            limite = datetime.now() + timedelta(days=365) 

            if data_final_convertida.date() < datetime.now().date() or data_final_convertida.date() > limite.date():

                print("\n ------------------------------------------------------------------ ")
                print("|     !!!  A data deve estar entre hoje até 1 ano à frente !!!     |")
                print(" ------------------------------------------------------------------ ")
                input("\n|  Pressione ENTER para tentar novamente...")
                continue

            if data_final_convertida < data_inicio_convertida:

                print("\n ------------------------------------------------------------------ ")
                print("|    !!!  A data final não pode ser menor que a data inicial !!!   |")
                print(" ------------------------------------------------------------------ ")
                input("\n|  Pressione ENTER para tentar novamente...")
                continue

            return data_final, data_final_convertida

        except ValueError: 

            print("\n ------------------------------------------------------------------ ")
            print("|     !!!  A data deve estar dentro no formado DD/MM/AAAA  !!!     |")
            print(" ------------------------------------------------------------------ ")
            input("\n|  Pressione ENTER para tentar novamente...")


# Subprograma (Função): Receber dificuldade ----------------------------------------------------------------------------

def receber_dificuldade():
    
    '''
    Recebe o nível de dificuldade da tarefa, validando
    a entrada para aceitar apenas valores inteiros
    entre 0 e 10.
    '''

    while True:

        try:

            dificuldade = int(input("\n|  Digite a dificuldade [0-10]: "))

            if 0 <= dificuldade <= 10:
                return dificuldade

        except ValueError:

            pass 

        print("\n ------------------------------------------------------------------ ")
        print("|           !!! Digite apenas valores de [0 a 10] !!!             |")
        print(" ------------------------------------------------------------------ ")
        input("\n|  Pressione ENTER para tentar novamente...")
            


# Subprograma (Função): Calcular Prioridade ---------------------------------------------------------------------------
def calcular_prioridade(dificuldade, data_final_convertida):
    
    '''
    Calcular automaticamente a prioridade da tarefa
    considerando o nível de dificuldade informado
    e a quantidade de dias restantes até o prazo final.
    '''    

    hoje = datetime.now().date()

    dias_restantes = (data_final_convertida.date() - hoje).days

    if dias_restantes > 10:
        dias_restantes = 10

    if dias_restantes < 0:
        dias_restantes = 0

    prioridade = dificuldade + (10 - dias_restantes)

    if prioridade > 10:
        prioridade = 10

    if prioridade < 0:
        prioridade = 0

    return prioridade


# Subprograma (Função): Cadastrar Tarefas ------------------------------------------------------------------------------
def cadastrar_tarefa(lista_tarefas):
    
    '''
    Receber as informações necessárias para o cadastro
    de uma nova tarefa, realizar as validações dos dados,
    calcular a prioridade automaticamente e adicionar
    a tarefa à matriz do sistema.
    '''

    while True:

        print("\n -------------------------------------------------------------------")
        print("|                         Cadastrar tarefa                          |")
        print(" -------------------------------------------------------------------")

        status = "Pendente"

        titulo = receber_titulo()

        descricao = receber_descricao()

        data_inicio, data_inicio_convertida = receber_data_inicio()

        data_final, data_final_convertida = receber_data_final(data_inicio_convertida)

        dificuldade = receber_dificuldade()

        prioridade = calcular_prioridade(dificuldade, data_final_convertida)

        tarefa = [
            status,
            titulo,
            descricao,
            data_inicio,
            data_final,
            dificuldade,
            prioridade
        ]

        lista_tarefas.append(tarefa) 
        salvar_tarefas(lista_tarefas) 

        print("\n ------------------------------------------------------------------ ")
        print("|            !!!  Tarefa cadastrada com sucesso  !!!               |")
        print(" ------------------------------------------------------------------ ")

        while True:

            continuar = input("\n|  Deseja cadastrar outra tarefa? [S/N]: ").upper() 

            if continuar == "S":

                break

            elif continuar == "N":

                return

            else:

                print("\n ------------------------------------------------------------------ ")
                print("|               !!!  Digite apenas S ou N  !!!                    |")
                print(" ------------------------------------------------------------------ ")
                input("\n|  Pressione ENTER para tentar novamente...")


# Subprograma (procedimento): Visualizar tarefas -----------------------------------------------------------------------
def visualizar_tarefas(lista_tarefas):

    '''
    Exibe todas as tarefas cadastradas no sistema,
    organizando-as automaticamente em ordem de
    prioridade e apresentando suas informações
    de forma estruturada ao usuário.
    ''' 

    print("\n ------------------------------------------------------------------ ")
    print("|                         Lista de tarefas                         |")
    print(" ------------------------------------------------------------------ ")


    if len(lista_tarefas) == 0:

        print("\n ------------------------------------------------------------------ ")
        print("|                 !!!  Nenhuma tarefa cadastrada  !!!              |")
        print(" ------------------------------------------------------------------ ")   
        return

    
    for i in range(len(lista_tarefas)):

        for j in range(len(lista_tarefas) - 1):

            if lista_tarefas[j][6] < lista_tarefas[j + 1][6]:

                lista_tarefas[j], lista_tarefas[j + 1] = lista_tarefas[j + 1], lista_tarefas[j]

    for i, tarefa in enumerate(lista_tarefas):

        print("\n|  Tarefa:", i + 1)

        print("\n|  Status:", tarefa[0])
        print("|  Título:", tarefa[1])
        print("|  Descrição:", tarefa[2])
        print("|  Data Início:", tarefa[3])
        print("|  Data Final:", tarefa[4])
        print("|  Dificuldade:", tarefa[5])
        print("|  Prioridade:", tarefa[6])
        print(" ------------------------------------------------------------------ ")

# Subprograma (procedimento): Editar Status ----------------------------------------------------------------------------
def editar_status(lista_tarefas):

    '''
    Permite concluir ou cancelar tarefas cadastradas,
    atualizando o status selecionado pelo usuário,
    removendo a tarefa da matriz e salvando as
    alterações realizadas no sistema.
    '''

    print("\n ------------------------------------------------------------------ ")
    print("|                    Concluir ou cancelar tarefas                  |")
    print(" ------------------------------------------------------------------ ")

    if len(lista_tarefas) == 0:

        print("\n ------------------------------------------------------------------ ")
        print("|              !!!  Nenhuma tarefa cadastrada  !!!                 |")
        print(" ------------------------------------------------------------------ ")
        input("\n|  Pressione ENTER para continuar...")
        
        return


    while True:

        try:

            visualizar_tarefas(lista_tarefas)

            numero_da_tarefa = int(input("\n|  Digite o número da tarefa que deseja editar: ")) - 1

            if 0 <= numero_da_tarefa < len(lista_tarefas):

                while True:

                    try:

                        print("\n ------------------------------------------------------------------ ")
                        print("|                     Atualizar status da tarefa                   |")
                        print("|                                                                  |")
                        print("|                1       |    Concluir tarefa                      |")
                        print("|                2       |    Cancelar tarefa                      |")
                        print(" ------------------------------------------------------------------ ")

                        opcao = int(input("\n|  Digite a opção: "))

                        if opcao == 1:

                            lista_tarefas[numero_da_tarefa][0] = "Concluída"


                        elif opcao == 2:

                            lista_tarefas[numero_da_tarefa][0] = "Cancelada"


                        else:

                            print("\n ------------------------------------------------------------------ ")
                            print("|                !!!  Digite [1 ou 2]  !!!                         |")
                            print(" ------------------------------------------------------------------ ")
                            input("\n|  Pressione ENTER para tentar novamente...")
                            continue


                        print("\n ------------------------------------------------------------------ ")
                        print("|         !!!  Status da tarefa atualizado com sucesso  !!!        |")
                        print(" ------------------------------------------------------------------ ")
                        break


                    except ValueError:

                        print("\n ------------------------------------------------------------------ ")
                        print("|                  !!!  Digite apenas números  !!!                 |")
                        print(" ------------------------------------------------------------------ ")
                        input("\n|  Pressione ENTER para tentar novamente...")


                del lista_tarefas[numero_da_tarefa] 
                salvar_tarefas(lista_tarefas) 
                break


            else:

                print("\n ------------------------------------------------------------------ ")
                print("|               !!!  Digite uma tarefa existente  !!!              |")
                print(" ------------------------------------------------------------------ ")
                input("\n|  Pressione ENTER para tentar novamente...")


        except ValueError:

            print("\n ------------------------------------------------------------------ ")
            print("|                    !!!  Digite apenas números  !!!               |")
            print(" ------------------------------------------------------------------ ")
            input("\n|  Pressione ENTER para tentar novamente...")


# Subprograma (Função): Editar Informações -----------------------------------------------------------------------------

def editar_informacoes(tarefas):

    '''
    Permite modificar informações de tarefas
    já cadastradas, atualizando os dados e
    recalculando automaticamente a prioridade
    quando necessário.
    '''

    print("\n ------------------------------------------------------------------ ")
    print("|                    Editar informações da tarefa                  |")
    print(" ------------------------------------------------------------------ ")

    if len(tarefas) == 0:

        print("\n ------------------------------------------------------------------ ")
        print("|             !!!  Nenhuma tarefa cadastrada  !!!                  |")
        print(" ------------------------------------------------------------------ ")

        input("\n|  Pressione ENTER para continuar...")
        return


    while True:

        try:

            visualizar_tarefas(tarefas)

            numero_da_tarefa = int(
                input("\n|  Digite o número da tarefa: ")
            ) - 1


            if 0 <= numero_da_tarefa < len(tarefas):

                while True:

                    try:

                        print("\n ------------------------------------------------------------------ ")
                        print("|                     Informações disponíveis                      |")
                        print("|                                                                  |")
                        print("|                         1     |    Título                        |")
                        print("|                         2     |    Descrição                     |")
                        print("|                         3     |    Data Final                    |")
                        print("|                         4     |    Dificuldade                   |")
                        print("|                         5     |    Data Início                   |")
                        print(" ------------------------------------------------------------------ ")

                        opcao = int(input("\n|  Digite a opção: "))


                        match opcao:

                            case 1:

                                tarefas[numero_da_tarefa][1] = receber_titulo()

                            case 2:

                                tarefas[numero_da_tarefa][2] = receber_descricao()

                            case 3:

                                data_inicio_convertida = datetime.strptime(tarefas[numero_da_tarefa][3], "%d/%m/%Y")

                                nova_data_final, nova_data_final_convertida = receber_data_final(data_inicio_convertida)

                                tarefas[numero_da_tarefa][4] = nova_data_final

                                tarefas[numero_da_tarefa][6] = calcular_prioridade(
                                    tarefas[numero_da_tarefa][5],
                                    nova_data_final_convertida
                                )

                            case 4:

                                nova_dificuldade = receber_dificuldade()

                                tarefas[numero_da_tarefa][5] = nova_dificuldade

                                data_final_convertida = datetime.strptime(tarefas[numero_da_tarefa][4], "%d/%m/%Y")

                                tarefas[numero_da_tarefa][6] = calcular_prioridade(nova_dificuldade, data_final_convertida)

                            case 5:

                                while True:

                                    nova_data_inicio, nova_data_inicio_convertida = receber_data_inicio()

                                    data_final_convertida = datetime.strptime(tarefas[numero_da_tarefa][4], "%d/%m/%Y")

                                    if nova_data_inicio_convertida > data_final_convertida:

                                        print("\n ------------------------------------------------------------------ ")
                                        print("|            !!!  Data início maior que data final  !!!            |")
                                        print(" ------------------------------------------------------------------ ")

                                        input("\n|  Pressione ENTER...")
                                        continue

                                    tarefas[numero_da_tarefa][3] = nova_data_inicio

                                    tarefas[numero_da_tarefa][6] = calcular_prioridade(
                                        tarefas[numero_da_tarefa][5],
                                        data_final_convertida
                                    )
                                    break

                            case _:

                                print("\n ------------------------------------------------------------------ ")
                                print("|                  !!!  Digite uma opção válida  !!!               |")
                                print(" ------------------------------------------------------------------ ")

                                input("\n|  Pressione ENTER...")
                                continue


                        salvar_tarefas(tarefas)

                        print("\n ------------------------------------------------------------------ ")
                        print("|          !!!  Informações atualizadas com sucesso  !!!           |")
                        print(" ------------------------------------------------------------------ ")

                        input("\n|  Pressione ENTER para continuar...")
                        return


                    except ValueError:

                        print("\n ------------------------------------------------------------------ ")
                        print("|                 !!!  Digite apenas números  !!!                  |")
                        print(" ------------------------------------------------------------------ ")
                        input("\n| Pressione ENTER...")

            else:

                print("\n ------------------------------------------------------------------ ")
                print("|             !!!  Digite uma tarefa existente  !!!                |")
                print(" ------------------------------------------------------------------ ")
                input("\n|  Pressione ENTER...")

        except ValueError:
            print("\n ------------------------------------------------------------------ ")
            print("|                   !!!  Digite apenas números  !!!                |")
            print(" ------------------------------------------------------------------ ")
            input("\n|  Pressione ENTER...")


# Programa Principal --------------------------------------------------------------------------------------------------
lista_tarefas = carregar_tarefas() #Atribuindo resultados carregados do txt para a matriz lista_tarefas
'''
Estrutura da matriz utilizada no sistema.

Cada linha corresponde a uma tarefa cadastrada,
e cada posição armazena uma informação específica:

    [0] Status
    [1] Título
    [2] Descrição
    [3] Data Início
    [4] Data Final
    [5] Dificuldade
    [6] Prioridade
'''

while True: 

    print("\n ------------------------------------------------------------------ ")
    print("|                             Menu                                 |")
    print(" ------------------------------------------------------------------ ")
    print("|     1      |    Cadastrar uma nova tarefa                        |")
    print("|     2      |    Visualizar lista de tarefas                      |")
    print("|     3      |    Concluir ou cancelar tarefas                     |")
    print("|     4      |    Editar outras informações das tarefas            |")
    print("|     5      |    Sair do Programa                                 |")
    print(" ------------------------------------------------------------------ ")

    try: 

        opcao = int(input("\n|  Digite a opção: "))

    except ValueError: 

        print("\n ------------------------------------------------------------------ ")
        print("|            !!!  Digite apenas valores de [1 a 5]  !!!            |")
        print(" ------------------------------------------------------------------ ")
        input("\n|  Pressione ENTER para tentar novamente...")
        continue

    match opcao: 

        case 1:

            cadastrar_tarefa(lista_tarefas)

        case 2:

            visualizar_tarefas(lista_tarefas)

        case 3:

            editar_status(lista_tarefas)

        case 4:

            editar_informacoes(lista_tarefas)

        case 5:
            
            while True:
                sair = input("\n|  Deseja realmente sair? [S/N]: ").upper()

                if sair == 'N':

                    break

                elif sair == 'S':

                    print("\n ------------------------------------------------------------------ ")
                    print("|                      Encerrando Programa...                      |")
                    print(" ------------------------------------------------------------------ \n")
                    
                    exit()

                else:

                    print("\n ------------------------------------------------------------------ ")
                    print("|               !!!  Digite apenas S ou N  !!!                    |")
                    print(" ------------------------------------------------------------------ ")

        case _:

            print("\n ------------------------------------------------------------------ ")
            print("|            !!!  Digite apenas valores de [1 a 5]  !!!            |")
            print(" ------------------------------------------------------------------ ")
            input("\n|  Pressione ENTER para tentar novamente...")
            continue

    input("\n|  Pressione ENTER para voltar ao menu...")