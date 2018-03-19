import sys
import time

temp1 = []

def get_input():
	fn = sys.argv[1]
	data = []
	with open(fn,'r') as f:
		while True:
			line = ""
			line = f.readline()
			if("" == line):
				break
			list = []
			list = line.split()
			list[0] = int(list[0])
			list[1] = int(list[1])
			data.append(list)
	f.close()
	return data

def compare(left, right):
	if(left <= right):
		return left
	return right

def get_min(data):
	min = -1
	for i in range(len(data)):
		for j in range(i+1,len(data)):
			temp = ((data[i][0] - data[j][0]) ** 2) + ((data[i][1] - data[j][1]) ** 2)
			temp = temp ** (.5)
			if(temp <= min or min == -1):
				min = temp
				temp1.append([[data[j][0], data[j][1], data[i][0], data[i][1]], temp])
	return min

def closeset_cross_pair(data, min):
	min_cross = -1
	for i in range(len(data)):
		for j in range(i+1, len(data)):
			if(data[j][1] - data[i][1] <= min):
				temp = ((data[i][0] - data[j][0]) ** 2) + ((data[i][1] - data[j][1]) ** 2)
				temp = temp ** (.5)
				if(temp <= min_cross or min_cross == -1):
					min_cross = temp
				temp1.append([[data[j][0], data[j][1], data[i][0], data[i][1]], temp])
			else:
				break
	if(min_cross == -1):
		return min
	return compare(min, min_cross)


def closeset_pair(data):
	if(len(data) <= 3):
		min = get_min(data)
		return min
	else:
		left = []
		right = []
		cross = []
		midPoint = len(data) / 2
		
		left = data[midPoint:]
		right = data[:midPoint]
		min_left = closeset_pair(left)
		min_right = closeset_pair(right)
		min = compare(min_left, min_right);
		
		left_limit = data[midPoint][0] - min
		right_limit = data[midPoint][0] + min
		for i in range(len(data)):
			if(data[i][0] >= left_limit and data[i][0] <= right_limit):
				cross.append(data[i])
			if(data[i][0] > right_limit):
				break
	#cross.sort(key = lambda s: s[1])
		minOfAll = closeset_cross_pair(cross, min)
		return minOfAll

def main():
	data = []
	data = get_input()
	data.sort()
	result = []
	min = closeset_pair(data)
	for i in range(len(temp1)):
		if (temp1[i][1] == min):
			if(temp1[i][0] not in result):
				result.append(temp1[i][0])
	result.sort()
	f = open("output_enhanceddnc.txt", 'w')
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




