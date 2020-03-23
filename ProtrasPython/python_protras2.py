import math
from functools import reduce


def euclidean_distance(x, y):
	finale_distance = 0
	for index in range(len(x)):
		finale_distance = finale_distance + math.pow((x[index] - y[index]), 2)
	return math.sqrt(finale_distance)


def protras(input_set, epsilon):
	first = True
	cost = 0

	coreset = []
	coreset.append(input_set[0])

	finale_core_attend = []

	while first is True or cost >= epsilon:
		temp = input_set
		coreattend = []

		for y in coreset:
			if y in temp:
				temp.remove(y)
			coreattend.append([])

		for x in temp:
			d_min = 1000000000000
			y_min = 0
			for y in range(len(coreset)):
				tmp = euclidean_distance(x, coreset[y])
				if tmp < d_min:
					d_min = tmp
					y_min = y
			if x not in coreattend[y_min]:
				coreattend[y_min].append(x)

		y_opt = 0
		x_max = [0 for z in range(len(coreset))]

		newly_cost = 0
		max_wd = 0

		for y in range(len(coreset)):
			d_max = 0
			for x in coreattend[y]:
				tmp = euclidean_distance(x, coreset[y])
				if tmp > d_max:
					d_max = tmp
					x_max[y] = x
			pk = (len(coreattend[y]) + 1) * d_max
			if pk > max_wd:
				max_wd = pk
				y_opt = y
			newly_cost = newly_cost + pk / len(input_set)

		x_opt = x_max[y_opt]
		if x_opt not in coreset:
			coreset.append(x_opt)
			coreattend.append([])

		first = False
		cost = newly_cost
		finale_core_attend = coreattend

	return cost, coreset, finale_core_attend


def convert_string_int(input_string):
	return reduce(lambda x, y: x + ord(y), input_string, 0)/100


def main():

	with open('ecoli1.dat', 'r') as input_file:
	# with open('Datasets/test','r+') as input_file:
		input_read = input_file.readlines()

	coordinate = []
	# for x in input_read[1:]:
	for x in input_read[12:]:
		temp = x.split("\n")[0]
		temp = temp.split(",")
		a = []
		for y in temp:
			a.append(convert_string_int(y))
		coordinate.append(a)

	cost, coreset, _ = protras(coordinate, 0.5)
	with open("Result\par.txt", 'a+') as output_result:
		output_result.write(str(cost) + "\t")
		output_result.write(str(coreset) + "\n")


if __name__ == "__main__":
	main()
