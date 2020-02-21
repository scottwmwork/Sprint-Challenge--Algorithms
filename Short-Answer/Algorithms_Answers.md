#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)


b)


c)

## Exercise II

### I would use binary search method
def find_max(n, f):
	
	# Base case
	if len(f) == 1:
		return f[0]
	
	n = len(f) // 2
	
	if egg_break(f[n]) == True:
		sub_list = f[:n]
		find_max(n, sub_list)
	else: 
		sub_list = f[n:]
		find_max(n, sub_list)		
		

The binary search would simply find the middle of the list and test if the egg breaks. If it does, then a new sublist is created and passsed recursively with the bounds adjusted downwards. Otherwise it will adjust upwards until the len of the list is 1 in which case the place in which the egg breaks is found. 
		

The complexity of this would be O(logn)

