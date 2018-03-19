import random
random.seed()
f = open("largeExample", 'w')
for i in range (1000000):
	x = random.randrange(10000)
	y = random.randrange(10000)
	f.write(str(x) + " " + str(y) + "\n")

f.close()
