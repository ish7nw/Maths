import numpy as np

np.random.seed(0)

A = np.random.randn(100, 2) @ np.random.randn(2, 50) + 0.01 * np.random.randn(100, 50)
# print(A)

U, S, Vt = np.linalg.svd(A, full_matrices=False) # this is the singular value decomposition happening
print(S[:5].round(3))

k = 2

A_k = U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :]          
print(np.linalg.norm(A - A_k) / np.linalg.norm(A))   
print(A.size, "->", U[:, :k].size + k + Vt[:k].size)