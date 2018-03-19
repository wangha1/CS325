import sys
import time

def main():
	fn = sys.argv[1]
	data = []
	min = -1
	result = [];
	temp1 = [];
	with open(fn, 'r') as f:
		while True:
			line = ""
			line = f.readline()
			if ("" == line):
				break
			list = []
			list = line.split()
			list[0] = int(list[0])
			list[1] = int(list[1])
			data.append(list)
	f.close()
	for i in range(len(data)):
		for j in range(i+1,len(data)):
			temp = ((data[i][0] - data[j][0]) ** 2) + ((data[i][1] - data[j][1]) ** 2)
			temp = temp ** (.5)
			if(temp <= min or min == -1):
				min = temp
				temp1.append([[data[j][0], data[j][1], data[i][0], data[i][1]], temp])
	for i in range(len(temp1)):
		if (temp1[i][1] == min):
			result.append(temp1[i][0])
	result.sort()
	f = open("output_bruteforce.txt", 'w')
	f.write(str(min));
	f.write("\n")
	for i in range(len(result)):
		f.write(str(result[i][0]) + " " + str(result[i][1]) + " " + str(result[i][2]) + " " + str(result[i][3]))
		f.write("\n")
	f.close()
	return 0

start_time = time.clock()
main();
print time.clock() - start_time, "seconds"
