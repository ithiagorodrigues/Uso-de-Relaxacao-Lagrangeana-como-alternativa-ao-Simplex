import gurobipy as gp

# Cria o modelo
m = gp.Model("Ex 1")

# Adiciona as variáveis no modelo
x1 = m.addVar()
x2 = m.addVar()

# Define a função objetivo
m.setObjective(-9 * x1 + 12 * x2, sense=gp.GRB.MAXIMIZE)

# Adiciona as restrições
c1 = m.addConstr(-x1+x2<=3)
c2 = m.addConstr(-4 *x1 + 5 * x2 <= 20)
c3 = m.addConstr(3 * x1 - 4 * x2 <=12)

# Executa o modelo
m.optimize()

# Imprime o plano de produção
print("Produto A:", x1.X)
print("Produto B:", x2.X)

