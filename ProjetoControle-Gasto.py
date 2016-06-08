import bibfuncao

print("""                        *** MENU ***
    *** Sistema de Controle de Gastos,hidráulicos ***
                    [1] Criar serviço
                    [2] Listar serviço
                    [3] Cadastrar cliente
                    [4] Procurar cliente
                    [5] Cadastrar funcionário
                    [6] Procurar Funcionário
                    [7] Sair """)

opcao=7
lista_servico=[]
lista_funcionario=[]



bibfuncao.menu()
entrada="S"
while opcao<=7:
    while entrada =="S":
        
        opcao=int(input("Qual opção deseja?"))
        while opcao<0:
            opcao=int(input("Ops! opção inválida, digite novamente"))
            
        if opcao==1:
            print(" *** CRIAR SERVIÇO ***")
            lista_servico.append(input(" Informe o serviço:"))
            
        elif opcao==2:
           print(" *** LISTAR TIPO DE SERVICO ***")
           for i in range(len(lista_servico)):
                    print(i+1,":"+lista_servico[i])
        elif opcao==3:
            print(" *** CADASTRAR CLIENTE ***")
            lista_servico.append(input(" Informe o nome do Cliente:"))
        
            for i in range(len(lista_servico)):
               print(i+1,":"+lista_servico[i])
        
        elif opcao==4:
            print(" *** PROCURAR CLIENTE ***")
            lista_servico.append(input(" Procurar  Cliente:"))
        
            for i in range(len(lista_servico)):
                print(i+1,":"+lista_servico[i])
        elif opcao==5:
            print(" *** CADASTRAR FUNCIONARIO ***")
            lista_funcionario.append(input("Cadastro do funcionário:"))
        
            for i in range(len(lista_funcionario)):
                print(i+1,":"+lista_funcionario[i])
            
        elif opcao==6:
            print(" *** PROCURAR FUNCIONARIO ***")
            lista_funcionario.append(input(" Procurar funcionario:"))
        
            for i in range(lista_funcionario):
                print(i+1,":"+lista_funcionario[i])
            
        elif opcao==7:
            print("Até a próxima!")
            entrada="N"
   
        else:
            print("Opção inválida! Digite apenas entre os números de 1 á 7.")
        if opcao!=7:
            entrada=input("Continuar? [S/N]:")

    



    
        

       
    
