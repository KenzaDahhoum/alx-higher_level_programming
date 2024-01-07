#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
	for r in matrix:
		for col in r:
			print("{:d}".format(col), end=" " if col != r[-1] else "")
		print()
