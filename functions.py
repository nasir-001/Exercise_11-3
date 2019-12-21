# Authur: Nasir Lawal
# Date: 21st-Dec-2019

"""
Write simple functions max2() and min2() that take
two items and return the larger and smaller item,
respectively
"""

def main():
	max_num(4, 8)
	max_num(8, 4)
	min_num(4, 8)
	min_num(8, 4)

def max_num(first, second):
	print(max(first, second))


def min_num(first, second):
	print(min(first, second))

if __name__ == "__main__":
	main()