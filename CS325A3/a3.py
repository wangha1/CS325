# READ ME
## Input file format as .xls, name Corvallis1.xls



import xlrd
import math
import pulp
import matplotlib.pyplot as plt


data = xlrd.open_workbook('Corvallis1.xls')
data.sheet_names()
sh = data.sheet_by_index(0)
i = 1
T = []
D = []
while (i<22305):
	T.append(sh.cell(i, 7).value)
	D.append(sh.cell(i, 8).value)
	i+=1

my_lp_problem = pulp.LpProblem("My LP Problem")
x0 = pulp.LpVariable('x0', cat='Continuous')
x1 = pulp.LpVariable('x1', cat='Continuous')
x2 = pulp.LpVariable('x2', cat='Continuous')
x3 = pulp.LpVariable('x3', cat='Continuous')
x4 = pulp.LpVariable('x4', cat='Continuous')
x5 = pulp.LpVariable('x5', cat='Continuous')
M = pulp.LpVariable('M', cat='Continuous')

my_lp_problem += M


for i in range(len(D)):
	my_lp_problem += (x0 + x1 * D[i] + x2 * math.cos((2*math.pi*D[i])/365.25) + x3 * math.sin((2*math.pi*D[i])/365.25) + x4 * math.cos((2*math.pi*D[i])/(365.25*10.7)) + x5 * math.sin((2*math.pi*D[i])/(365.25*10.7))) - T[i] >= -M
	my_lp_problem += (x0 + x1 * D[i] + x2 * math.cos((2*math.pi*D[i])/365.25) + x3 * math.sin((2*math.pi*D[i])/365.25) + x4 * math.cos((2*math.pi*D[i])/(365.25*10.7)) + x5 * math.sin((2*math.pi*D[i])/(365.25*10.7))) - T[i] <= M


my_lp_problem.solve()
print(pulp.LpStatus[my_lp_problem.status])
for variable in my_lp_problem.variables():
	print "{} = {}".format(variable.name, variable.varValue)


plt.plot(D,T)



coef0 = x0.varValue
coef1 = x1.varValue
coef2 = x2.varValue
coef3 = x3.varValue
coef4 = x4.varValue
coef5 = x5.varValue

T1 = []
D1 = []
for i in range(22305):
	temp = coef0 + coef1 * i + coef2 * math.cos((2*math.pi*i)/365.25) + coef3 * math.sin((2*math.pi*i)/365.25) + coef4 * math.cos((2*math.pi*i)/(365.25*10.7)) + coef5 * math.sin((2*math.pi*i)/(365.25*10.7))
	T1.append(temp)
	D1.append(i)

T2 = []
D2 = []
for i in range(22305):
	temp = coef0 + coef1 * i
	T2.append(temp)
	D2.append(i)



plt.plot(D1,T1)



plt.plot(D2,T2)

plt.grid(True)

plt.show()











































