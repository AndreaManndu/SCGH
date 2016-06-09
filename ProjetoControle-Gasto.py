
import bibfuncao

print("""                        *** MENU ***
    *** Sistema de Controle de Gastos,hidráulicos ***
                    [1] Criar serviço
                    [2] Listar serviço
                    [3] Procurar cliente
                    [4] Procurar Funcionário
                    [5] Sair """)

opcao=5

servicos=[]
clientes=[]
funcionarios=[]


entrada="S"
while opcao<=5:
    while entrada =="S":
        
        opcao=int(input("Qual opção deseja?"))
        while opcao<0:
            opcao=int(input("Ops! opção inválida, digite novamente"))
        if opcao==1:
            print(" *** CRIAR SERVIÇO ***")
            nomeServico=input("Informe o serviço: ")
            #servicos.append(nomeServico)
            Qtd_clientes=int(input("Quantidade de cliente: "))
            for i in range (Qtd_clientes):
                nome_cliente=input("Nome do cliente: ")
                clientes.append(nome_cliente)
            #servicos.append(clientes)
                
            Qtd_funcionario=int(input("Quantidade funcionario: "))
            for i in range (Qtd_funcionario):
                nome_funcionario=input("Nome funcionario: ")
                salario = float(input("Informe o salário: "))
                funcionarios.append([nome_funcionario, salario])
            #servicos.append(funcionarios)
            servicos.append([nomeServico, clientes, funcionarios])
            print(servicos)
        #FAZER        
        elif opcao==2:
            print(" *** LISTAR TIPO DE SERVICO ***")
            for i in range(len(servicos)):
                print(servicos[i][0])

        #FAZER
        elif opcao==3:
            
            print(" *** PROCURAR CLIENTE ***")
        #FAZER
        elif opcao==4:
            print(" *** PROCURAR FUNCIONARIO ***")
            
        elif opcao==5:
            print("Até a próxima!")
            entrada="N"
        else:
            print("Opção inválida! Digite apenas entre os números de 1 á 7.")
        if opcao!=5:
            entrada=input("Continuar? [S/N]:")

    



    
        

       
    
