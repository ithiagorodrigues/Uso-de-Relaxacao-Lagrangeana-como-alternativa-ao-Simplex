import gurobipy as gp
import numpy as np

def ler_arquivo(nome_arq): #Leitura e tratamento dos dados

    with open(nome_arq,'r+') as file:
        linhas =        file.readlines(); #Passa o arquivo inteiro para a lista linhas
        dados =         linhas[0].strip().split(" ") #Responsavel por receber os dados do grafo
        qtd_nos =       int(dados[0]) #Quantidade de Nós
        custo = list()
        custo = np.zeros((qtd_nos,qtd_nos),dtype=np.int) #Matriz de custos
        qtd_arestas =  int(dados[1]) #Quantidade de arestas do grafo
        saida =         int(dados[2]) #Vertice de origem
        chegada =       int(dados[3]) #Vertice de chegada
        inicio =        dict() #Aretas que chegam
        destino =       dict() #Aretas que saiem
        del(linhas[0]) #Remove a linha com dados do grafo
        
        #Tratamento dos dados
        for linha in linhas: 
            u, v,p =  map(int, linha.strip().split(' '))
            if u not in inicio:
                inicio[u] = [v]
                custo[u-1][v-1]=p
            else:
                inicio[u].append(v)
                custo[u-1][v-1]=p
                pass
        for linha in linhas:
            u, v, p =  map(int, linha.strip().split(' '))
            if v not in destino:
                destino[v] = [u]
            else:
                destino[v].append(u)
                pass

    pass
    custoList = custo.tolist()
    file.close()
    return qtd_nos, qtd_arestas,saida,chegada,inicio, destino,custo,custoList
pass

# Recebimento dos dados
qtd_nos, qtd_arestas,saida,chegada,inicio,destino,custo,custoList = ler_arquivo(".\Fluxo Maximo\dados_000.txt") 

# #Prints
# print(" Quantidade de nos: ",qtd_nos, "\n","Quantidade de arestas: ",qtd_arestas,"\n","Saida: ",saida,"\n","Chegada:",chegada,"\n")

# print('Inicio\n')
# for custos,teste in inicio.items():
#     print(custos,teste)
# print('\nDestino\n')
# for custos,teste in destino.items():
#     print(custos,teste)
# print("\nMatriz de Custos\n\n",custo)
# #Prints

def meio(modelo,i):
    c1 = m.addConstr(
        gp.quicksum(x[saida, j] for j in destino if saida != j) == gp.quicksum(x[i, chegada] for i in inicio if i != chegada)
        )

    pass


m = gp.Model()

x = m.addVars(8, 8, vtype=gp.GRB.BINARY)
# print(x)

m.setObjective(x.prod(custoList), sense=gp.GRB.MAXIMIZE)

c2 = m.addConstr(
        gp.quicksum(x[saida, j] for j in destino if saida != j) == 1 
        )
    

for i in range(qtd_nos):
    if( i != saida and i != chegada):
        meio(m,i)
    pass

c3 = m.addConstr(
        gp.quicksum(x[i, chegada] for i in inicio if i != chegada) == 1 
        )

m.optimize()

circuito = [1]
anterior = 1
for ponto in range(7):
    for j in destino:
        if round(x[anterior, j].X) == 1:
            circuito.append(j)
            anterior = j
            break
print(circuito)
for i in inicio:
    print("{:02d}: ".format(i), end="")
    for j in destino:
        print(round(x[i, j].X), "", end="")
    print("")