import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

t = sp.Symbol('t')
a = 1

# Paramétricas
x = a * (2 * sp.cos(t) - sp.cos(2*t))
y = a * (2 * sp.sin(t) - sp.sin(2*t))

# Derivada
dx_dt = sp.diff(x, t)

# Área
integrando = y * dx_dt

area = abs(sp.integrate(integrando, (t, 0, sp.pi)))

print("Área =", area)

# Parte numérica para graficar
t_num = np.linspace(0, 2*np.pi, 1000)

x_num = a * (2*np.cos(t_num) - np.cos(2*t_num))
y_num = a * (2*np.sin(t_num) - np.sin(2*t_num))

# Gráfica
plt.figure(figsize=(7,7))

plt.plot(x_num, y_num, color='red')

plt.axhline(0, color='black')
plt.axvline(0, color='black')

plt.grid(True)
plt.axis('equal')

plt.title("Cardioide")

plt.show()