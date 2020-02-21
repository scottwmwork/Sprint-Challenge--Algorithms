#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) **O(n)** - This would almost appear to be O(n^3) however, the extra `n`'s are canceled by `a = a + n * n` which rapidly decreases the amount it take for `a` to be greater than or equal to `n`


b) **O(nlogn)** - Since the second loop is not growing by 1 but rather doubles, as `n` grows, the second loop takes less time to complete. The first loop take `n` times to complete thus giving `n * log(n)`


c) **O(n)** - The function is recursively called the number of bunnies there are since `bunnies-1` is called until the base case is reached where `bunnies == 0`

## Exercise II

### I would use binary search method

The binary search would simply find the middle of the list and test if the egg breaks. If it does, then a new sublist is created and passsed recursively with the bounds adjusted downwards. Otherwise it will adjust upwards until the len of the list is 1 in which case the place in which the egg breaks is found. 
		

The complexity of this would be O(logn)

