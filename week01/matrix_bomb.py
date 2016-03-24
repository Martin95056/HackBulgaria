import pprint
import copy

NEIGHBORS = [(-1, -1), (-1, 0), (-1, 1),
			(0, -1), (0, 0), (0, 1),
			(1, -1), (1, -1), (1, 1)]

def sum_matrix(matrix):
	return sum([sum(row) for row in matrix])

def in_bounds(matrix, pos):
	if pos[0] >= len(matrix) or pos[0] < 0:
		return False
	
	if pos[1] >= len(matrix[0]) or pos[1] < 0:
		return False

	return True

def bomb(matrix, at):
	if in_bounds(matrix, at) == False:
		return natrix

	target = matrix[at[0]][at[1]]
	x, y = 0, 1

	for position in NEIGHBORS:
		position = (at[x] + position[x], at[y] + position[y])
		if in_bounds(matrix, position) == True:
			position_value = matrix[position[x]][position[y]]
			matrix[position[x]][position[y]] -= min(target, position_value)

		return matrix

def matrix_bombing_plan(matrix):
	result = {}
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			bombed = bomb(copy.deepcopy(matrix), (i, j))
			result[(i, j)] = sum_matrix(bombed)

	return result

def main():
	m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	result = matrix_bombing_plan(m)

	pp = pprint.PrettyPrinter()
	pp.pprint(result)

if __name__ == "__main__":
	main()
