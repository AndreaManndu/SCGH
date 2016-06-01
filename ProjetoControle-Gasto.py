print("""                        *** MENU ***
    *** Sistema de Controle de Gastos,hidráulicos ***
                    [1] Criar serviço
                    [2] Listar serviço
                    [3] Cadastrar cliente
                    [4] Procurar cliente
                    [5] Cadastrar funcionário
                    [6] Procurar Funcionário
                    [7] Sair """)

opcao=0
dados=[]

while opcao!=7:
    
    opcao=int(input("Qual opção deseja?"))
    if opcao==1:
        print(" *** CRIAR SERVIÇO ***")
        
        entrada="S"
        while entrada =="S":
            
            dados.append(input(" Informe o serviço:"))
            

            entrada=input("Coninuar? [S/N]:")
          
           
    elif opcao==2:
        
        print(" *** LISTAR TIPO DE SERVICO ***")
        
        for i in range(len(dados)):
            
            print(i+1,":"+dados[i])
            
    elif opcao==3:
        
        print(" *** CADASTRAR CLIENTE ***")
        
        dados.append(input(" Informe o nome do Cliente:"))
        
        for i in range(len(dados)):
            
            print(i+1,":"+dados[i])
        
    elif opcao==4:
        
        print(" *** PROCURAR CLIENTE ***")
        
        dados.append(input(" Procurar  Cliente:"))
        
        for i in range(len(dados)):
            
            print(i+1,":"+dados[i])
            
    elif opcao==5:
        
        print(" *** CADASTRAR FUNCIONARIO ***")
        
        dados.append(input("Cdastro do funcionário:"))
        
        for i in range(len(dados)):
            
            print(i+1,":"+dados[i])
            
    elif opcao==6:
        
        print(" *** PROCURAR FUNCIONARIO ***")
        
        dados.append(input(" Procurar funcionario:"))
        
        for i in range(len(dados)):
            
            print(i+1,":"+dados[i])
            
    elif opcao==7:
        
        print("Até a próxima!")
   
    else:
        print("Opção inválida! Digite apenas entre os números de 1 á 7.")



    
        

       
    
