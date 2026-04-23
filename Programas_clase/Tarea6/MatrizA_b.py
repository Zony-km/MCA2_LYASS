import numpy as np

# Matriz del sistema (b)
A = np.array([
    [1, 1, 1, 1],
    [1.01, 1.02, 1.03, 1.04],
    [1.01**2, 1.02**2, 1.03**2, 1.04**2],
    [1.01**3, 1.02**3, 1.03**3, 1.04**3]])

# Inversa
A_inv = np.linalg.inv(A)

print("A inversa:\n", A_inv)

# Norma L1
norm1 = np.linalg.norm(A, 1)
norm1_inv = np.linalg.norm(A_inv, 1)
kappa1 = norm1 * norm1_inv

print("\nNorma L1 de A:", norm1)
print("Norma L1 de A^-1:", norm1_inv)
print("kappa_1:", kappa1)

# Norma infinito
norm_inf = np.linalg.norm(A, np.inf)
norm_inf_inv = np.linalg.norm(A_inv, np.inf)
kappa_inf = norm_inf * norm_inf_inv

print("\nNorma infinito de A:", norm_inf)
print("Norma infinito de A^-1:", norm_inf_inv)
print("kappa_inf:", kappa_inf)