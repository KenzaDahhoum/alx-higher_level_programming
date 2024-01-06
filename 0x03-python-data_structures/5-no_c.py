#!/usr/bin/env python3

def no_c(my_string):
	n_string = ""

	for char in my_string:
		if char not in ('c', 'C'):
			n_string += char

	return (n_string)
