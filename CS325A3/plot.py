import xlrd
import math
import pulp
import matplotlib.pyplot as plt

x = [1,2,3,5,7,8,10]
y = [3,5,7,11,14,15,19]

x1 = []
y1 = []
for i in range (11):
	temp = 1.714286 * i + 1.857143
	x1.append(i)
	y1.append(temp)

plt.subplot(221)
plt.plot(x,y)

plt.grid(True)

plt.subplot(221)
plt.plot(x1,y1)



plt.show()
