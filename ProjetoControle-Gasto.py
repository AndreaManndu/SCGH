import bibfuncao


opcao=5

servicos=[]
clientes=[]
funcionarios=[]

bibfuncao.menu()
entrada="S"
while opcao<=5:
    while entrada =="S":
        
        opcao=int(input("Qual opção deseja?"))
        while opcao<0:
            opcao=int(input("Ops! opção inválida, digite novamente"))
        if opcao==1:
            print(" *** CRIAR SERVIÇO ***")
            nomeServico=input("Informe o serviço: ")
         
            Qtd_clientes=int(input("Quantidade de cliente: "))
            for i in range (Qtd_clientes):
                nome_cliente=input("Nome do cliente: ")
                clientes.append(nome_cliente)
                
            Qtd_funcionario=int(input("Quantidade funcionario: "))
            for i in range (Qtd_funcionario):
                nome_funcionario=input("Nome funcionario: ")
                salario = float(input("Informe o salário: "))
                funcionarios.append([nome_funcionario, salario])
            
            servicos.append([nomeServico, clientes, funcionarios])
            print(servicos)
             
        elif opcao==2:
            bibfuncao.listar_servico(servicos)
            
        elif opcao==3:

            bibfuncao.procurar_cliente(servicos)
        
        elif opcao==4:
            bibfuncao.procurar_funcionario(servicos)
            
        elif opcao==5:
            print("Até a próxima!")
            entrada="N"
        else:
            print("Opção inválida! Digite apenas entre os números de 1 á 5.")
        if opcao!=5:
            entrada=input("Continuar? [S/N]:")

    



    
        

       
    
