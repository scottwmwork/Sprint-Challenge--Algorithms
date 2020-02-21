def count_th(word):
	count = []

	def find_th(n):
		# Base case 1
		if n < 0:
			return
		if word[n] == 't' and word[n + 1] == 'h':
			count.append('')
		
		find_th(n - 1)

	find_th(len(word)-2)
	return len(count)

