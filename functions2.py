#Authur: Nasir Lawal
#Date: 21st-Dec-2019

"""
Create new functions my_max() and my_min() that use
your solutions in part (a) to recreate max() and min().
These functions return the largest and smallest item of
non-empty sequences, respectively.
"""
import functions


def main():
	my_max(4, 8)
	my_max(8, 4)
	my_min(4, 8)
	my_min(8, 4)
	more_arguments()
	user_input()


def my_max(first, second):
	functions.max_num(first, second) # Inherits max_num from functions.py module


def my_min(first, second):
	functions.min_num(first, second) # Inherits min_num from functions.py module


def more_arguments(*args): # more argument it can be str or integers argument
	alphabets = ['A', 'B', 'C', 'D']
	print(min(alphabets))


if __name__ == "__main__":
	main()