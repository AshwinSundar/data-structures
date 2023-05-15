import numpy as np # for testing only
from typing import Optional

# derived from ndArray to get access to existing member functions
class DerivedArray(np.ndarray): 
	# implemented via operator override
	# algorithm complexity is cubic O(i*j*k)
	# (DerivedArray) -> Opt(DerivedArray)
	def __mul__(self, other: type['DerivedArray']) -> Optional['DerivedArray']:
		if not self.canMultiply(other):
			return None
		else:
			output = DerivedArray((len(self), len(other[0]))) # rows of A x cols of B
			output.fill(0)

			for i in range(len(self)): # each row in self
				for j in range(len(other[0])): # each column in other
					sum = 0
					for k in range(len(self[0])): # each column in self
						sum += self[i][k] * other[k][j]
					output[i][j] = sum

			return output
	
	# (DerivedArray) -> bool
	def canMultiply(self, other: type['DerivedArray']) -> bool:
		return True if len(self[0]) == len(other) else False

	# fills random ints [1 - 10]
	# () -> ()
	def fillRandom(self):
		rng = np.random.default_rng(None) # initialize random number generator
		for r in range(len(self)):
			for c in range(len(self[0])):
				self[r][c] = rng.integers(low = 0, high = 10)

def test_DerivedArray():
	da11 = DerivedArray((1,1))
	da12 = DerivedArray((1,2))
	da21 = DerivedArray((2,1))
	da22 = DerivedArray((2,2))
	da11.fill(1)
	da12.fill(1)
	da21.fill(1)
	da22.fill(1)

	assert da11.canMultiply(da11) == True
	assert da11.canMultiply(da21) == False
	assert da22.canMultiply(da21) == True
	assert da21.canMultiply(da22) == False
	assert da21.canMultiply(da11) == True

	na11 = np.ndarray((1,1))
	na12 = np.ndarray((1,2))
	na21 = np.ndarray((2,1))
	na22 = np.ndarray((2,2))
	na11.fill(1)
	na12.fill(1)
	na21.fill(1)
	na22.fill(1)

	assert da11*da11 == np.matmul(na11, na11) # check against numpy matrix multiplication
	assert da12*da21 == np.matmul(na12, na21) 
	assert (da21*da12 == np.matmul(na21, na12)).all() # output is an array of bools, .all() compresses to single [bool]
	assert (da22*da22 == np.matmul(na22, na22)).all()
	

def fuzzTesting():
	da33 = DerivedArray((3,3))
	da33.fillRandom()
	na33 = np.ndarray((3,3))
	
	for r in range(len(da33)):
		for c in range(len(da33[0])):
			na33[r,c] = da33[r,c]

	print("da33 = \n", da33)
	print("na33 = \n", na33)

	daMultAns = da33*da33
	naMultAns = np.matmul(na33, na33)

	print("da33*da33 = \n", daMultAns)
	print("na33*na33 = \n", naMultAns)

	assert (daMultAns == naMultAns).all()

test_DerivedArray()
fuzzTesting()
