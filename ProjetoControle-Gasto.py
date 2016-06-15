import bibfuncao

arquivoClientes = "arquivoClientes.txt"
arquivo = open(arquivoClientes, "a")

opcao=5

servicos=[]
clientes=[]
funcionarios=[]
materiais=[]
despesas_administrativa=[]

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
                bibfuncao.cliente(arquivo, arquivoClientes, nome_cliente)
                clientes.append(nome_cliente)
                
                #DESPESAS COM FUNCIONARIOS
            
            Qtd_funcionario=int(input("Quantidade funcionario: "))
            
            for i in range (Qtd_funcionario):
                
                nome=input("Nome funcionario: ")
                
                cargo=input("Cargo do funcionário:")
                
                idade=int(input("Digite a idade do funcionário:"))
                
                salario = float(input("Informe o salário: "))
                
                cpf=int(input("Digite o CPF do funcionário:"))
                
                transporte=float(input("Informe o valor gasto com  transporte:"))
                
                alimentacao=float(input("Informe o valor gasto com alimentação:"))
                
                despesa_func= Qtd_funcionario + salario + transporte + alimentacao
                
                funcionarios.append([nome,cargo,salario,idade,cpf,transporte,alimentacao])
                print("Total  gasto com funcionário foi",despesa_func)
    # Despesas com materiais do serviço
            Qtd_material=int(input("Informe a quantidade de materiais, para este serviço:"))
            for i in range(Qtd_material):
                tipo_material=input("Informe o tipo de material:")
                valor_material=float(input("Digite o valor do material:"))
                calculo_materiais= Qtd_material * valor_material
                materiais.append([tipo_material, valor_material])
                print("Total do valor gasto com os materias:",calculo_materiais)
            servicos.append([nomeServico, clientes, funcionarios,materiais])
            print(servicos)
            

                
    # Despesas  administrativas
                
            
            Qtd_contador=int(input("Quantidade de contador:"))
            for i in range(Qtd_contador):
                contador=(input("Nome do contador da empresa:"))
                salario=float(input("Digite o salário:"))
                transporte=float(input("valor transporte:"))
                alimentacao=float(input("Valor alimentação:"))
                totalGasto= salario + transporte + alimentacao
                despesas_administrativa.append([contador,salario,transporte,alimentacao])
                print("Valor gasto com o contador é:", totalGasto)
            
                
            Qtd_materiais=int(input("Digite a quantidade de materias administrativos:"))
            for i in range (Qtd_materiais):
                nome=input("Nome do item:")
                valor=float(input("Valor do item:"))
                total_material= Qtd_materiais + valor
                despesas_administrativa.append([nome,valor])
                print("Valor gasto com materias administrativos é:",total_material)
            print(despesas_administrativa)

            orcamento_servico= despesa_func + calculo_materiais + totalGasto +  total_material
            print("Total gasto com todo o serviço:", orcamento_servico)
            
       # Chamando funções         
                  
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

    



    
        

       
    
