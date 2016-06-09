

def menu():
   print("""                        *** MENU ***
    *** Sistema de Controle de Gastos,hidráulicos ***
                    [1] Criar serviço
                    [2] Listar serviço
                    [3] Procurar cliente
                    [4] Procurar Funcionário
                    [5] Sair """)


    
    



def listar_servico(servicos):
    print(" *** LISTAR TIPO DE SERVICO ***")
    for i in range(len(servicos)):
        print(i+1, " - " , servicos[i][0])
    


def procurar_cliente(servicos):
    print(" *** PROCURAR CLIENTE ***")
    procura_cliente=input("Informe o nome do cliente que quer enontrar:")
    cont=0
    for i in range(len(servicos)):
        if servicos[i][1][i]==procura_cliente: # Cada [i] pega uma sublista
            cont+=1
            print(cont,"-",servicos[i][1][i])

def procurar_funcionario(servicos):
    print(" *** PROCURAR FUNCIONARIO ***")
    procura_funcionario=input("Informe o funcionaio que deseja enconttrar:")
    cont=0
    for i in range(len(servicos)):
        if servicos[i][2][i][0]==procura_funcionario:
            cont+=1
            print(cont,"-",servicos[i][2][i][0])# COMO TENHO UMA SUBLISTA DE FUNCIONARIO, USO O [I] PARA PEGAR CADA SUBLISTA*
                    

    
    
     
    
