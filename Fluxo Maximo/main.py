import gurobipy as gp

mat_custos = [
    [ 1,  2,  3,  4,  5,  6, 7]
    [ 0,  6,  4,  1,  0,  0,  0],
    [-1,  0, -1,  0,  4,  0,  0],
    [ 4, -1,  0, -1,  1, -1, -1],
    [ 1, -1,  3,  0, -1,  9, -1],
    [-1,  4,  1, -1, -1, -1,  4],
    [-1, -1,  3,  4, -1, -1,  9],
    [-1, -1, -1, -1, -1, -1, -1],
]

origens = 1
destinos = 7
custos = dict()

for i, origen in enumerate(origens):
    for j, destino in enumerate(destinos):
        custos[origen,destino] = mat_custos[i][j]

def meio(modelo,i):
    c1 = m.addConstrs(
        gp.quicksum(x[i, j] for j in destinos if i != j) == gp.quicksum(x[i, j] for i in origens if i != j )
        )

    pass


m = gp.Model()

x = m.addVars(origens, destinos, vtype=gp.GRB.BINARY)
u = m.addVars(origens, vtype=gp.GRB.INTEGER)
inicio = m.addVar()

mDestino = m.addVars(destinos, vtype=gp.GRB.INTEGER)

m.setObjective(x.prod(custos), sense=gp.GRB.MAXIMIZE)

c2 = m.addConstrs(
        gp.quicksum(x[origens, j] for j in destinos if i != j) == 1
        )
    

for i in origens:
    meio(m,i);
    pass

c3 = m.addConstrs(
        gp.quicksum(x[i, destinos] for j in destinos if i != j) == 1
        )

m.optimize()


circuito = [1]
anterior = 1
for ponto in range(7):
    for j in destinos:
        if round(x[anterior, j].X) == 1:
            circuito.append(j)
            anterior = j
            break
print(circuito)
for i in origens:
    print("{:02d}: ".format(i), end="")
    for j in destinos:
        print(round(x[i, j].X), "", end="")
    print("")