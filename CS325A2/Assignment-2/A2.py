# READ ME
## Execute use this command: python A2.py
### Take default file name imp2cost.txt and imp2input.txt as input
#### NO FILE NAME AS PARAMETERS
##### IF DIFFERENT INPUT FILE NAME PLEASE MODIFY YOUR FILE NAME OR "cost" VARIABLE AND "input" VARIABLE IN PROGRAM
###### CS325 assignment2
####### Writen by Hao Wang


import sys
import time

cost = "imp2cost.txt"
costMatrix = []
with open(cost, 'r') as f:
	temp = f.read().splitlines()
	for line in temp:
		subLine = line.split(",")
		del subLine[0]
		costMatrix.append(subLine)
del costMatrix[0]
f.close()

def main():
	fn = open("imp2output.txt", 'w')
	fn.write("")
	fn.close()
	input = "imp2input.txt"
	with open(input, 'r') as f:
		temp = f.read().splitlines()
		for line in temp:
			string = line.split(",")
			str1 = string[0]
			str2 = string[1]
			Align(str1, str2)
	f.close()
	return 0

def getCost(s1, s2):
	if(s1 == "-"):
		i = 0
	elif(s1 == "A"):
		i = 1
	elif(s1 == "T"):
		i = 2
	elif(s1 == "G"):
		i = 3
	elif(s1 == "C"):
		i = 4
	if(s2 == "-"):
		j = 0
	elif(s2 == "A"):
		j = 1
	elif(s2 == "T"):
		j = 2
	elif(s2 == "G"):
		j = 3
	elif(s2 == "C"):
		j = 4
	return int(costMatrix[i][j])


def Align(str1, str2):
	m = len(str1) + 1
	n = len(str2) + 1

	D = {}
	ptr = {}
	D[0, 0] = 0
	for i in range(1, m):
		D[i, 0] = getCost(str1[i - 1], "-") + D[i - 1, 0]
		ptr[i, 0] = 2
	for j in range(1, n):
		D[0, j] = getCost("-", str2[j - 1]) + D[0, j - 1]
		ptr[0, j] = 1

	finaStr1 = ""
	finaStr2 = ""

	for i in range(1, m):
		for j in range(1,n):
			cost = getCost(str1[i - 1], str2[j - 1])
			D[i, j] = min(D[i, j - 1] + getCost("-", str2[j - 1]), D[i - 1, j] + getCost(str1[i - 1], "-"), D[i - 1, j - 1] + cost)
			if(D[i , j] == D[i, j - 1] + getCost("-", str2[j - 1])):
				ptr[i, j] = 1
			elif(D[i , j] == D[i - 1, j] + getCost(str1[i - 1], "-")):
				ptr[i, j] = 2
			else:
				ptr[i, j] = 3
	mindis = D[i, j]
	while True:
		if( i == 0 and j == 0):
			break
		if(ptr[i, j] == 1):
			finaStr1 += "-"
			finaStr2 += str2[j - 1]
			j -= 1
		elif(ptr[i, j] == 2):
			finaStr1 += str1[i - 1]
			finaStr2 += "-"
			i -= 1
		else:
			finaStr1 += str1[i - 1]
			finaStr2 += str2[j - 1]
			i -= 1
			j -= 1

	fn = open("imp2output.txt", 'a')
	fn.write((finaStr1[::-1]) + "," + (finaStr2[::-1]) + ":" + (str(mindis)))
	fn.write("\n")
	fn.close()
	return mindis

main();














