import random


f = open("largeinput.txt", 'w')
random.seed()
for j in range(5000):
	x = random.randrange(4)
	if(x == 0):
		f.write("A")
	elif(x == 1):
		f.write("T")
	elif(x == 2):
		f.write("G")
	elif(x == 3):
		f.write("C")
f.write(",")
for j in range(5000):
	x = random.randrange(4)
	if(x == 0):
		f.write("A")
	elif(x == 1):
		f.write("T")
	elif(x == 2):
		f.write("G")
	elif(x == 3):
		f.write("C")
f.write("\n")
