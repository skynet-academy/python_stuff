import pylab
import random

SAMPLE_SIZE = 1000

# seed random generator
# if no argument provided
# uses system current time

random.seed()

# store generated random values here

real_rand_vars = []

# pick some random values

real_rand_vars = [random.randint(1,1000) for val in range(SAMPLE_SIZE)]

pylab.hist(real_rand_vars, 10)

# define x and y labels 

pylab.xlabel("Number range")
pylab.ylabel("Count")

# show figure

pylab.show()
