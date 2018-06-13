import random

a = 1; b = 6
r1 = random.randint(a, b) 	# first die
r2 = random.randint(a, b) 	# second die

print('The dice gave:  {:d} and {:d}'.format(r1, r2))
