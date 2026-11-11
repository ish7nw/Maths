import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a@b) # this is just a regular dot product 
print(np.dot(a,b)) # this is also the same thing

print(np.outer(a,b)) # this is an outer product

'''
What an outer product does is, it takes each element from one matrix and multiplies it by all the elements
one by one from another matrix so for the above example [4, 5, 6] gets multiplied by 1 and that becomes the first row, 
then [4, 5, 6] by 2 and that becomes the second row....
'''


A, B = a.reshape(3, 1), b.reshape(3, 1)
print(A)
print()
print(B)
print()
print(A.T@B)
print()
print(A@B.T)
print()
print((A@B.T).shape)

