import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Visualización de cuatro hiperplanos reducidos a 3D fijando x4 = 0.

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(projection='3d')

# Rango para las variables x1 y x3
x1 = np.linspace(0, 10, 50)
x3 = np.linspace(0, 10, 50)
X1, X3 = np.meshgrid(x1, x3)

# Valor fijo para x4
x4 = 0

# Planos obtenidos al despejar x2:
#   Ecuación 1:  x1 + x2 + x3 + x4 = 10
#   Ecuación 2:  1.01x1 + 1.02x2 + 1.03x3 + 1.04x4 = 20
#   Ecuación 3:  (1.01^2)x1 + (1.02^2)x2 + (1.03^2)x3 + (1.04^2)x4 = 30
#   Ecuación 4:  (1.01^3)x1 + (1.02^3)x2 + (1.03^3)x3 + (1.04^3)x4 = 40

Z1 = 10 - X1 - X3 - x4
Z2 = (20 - 1.01*X1 - 1.03*X3 - 1.04*x4) / 1.02
Z3 = (30 - (1.01**2)*X1 - (1.03**2)*X3 - (1.04**2)*x4) / (1.02**2)
Z4 = (40 - (1.01**3)*X1 - (1.03**3)*X3 - (1.04**3)*x4) / (1.02**3)

# Representación de las superficies
ax.plot_surface(X1, X3, Z1, alpha=0.4, color='red', edgecolor='none')
ax.plot_surface(X1, X3, Z2, alpha=0.4, color='blue', edgecolor='none')
ax.plot_surface(X1, X3, Z3, alpha=0.4, color='green', edgecolor='none')
ax.plot_surface(X1, X3, Z4, alpha=0.4, color='purple', edgecolor='none')

# Ajuste de vista 3D
ax.view_init(elev=30, azim=135)

# Etiquetas de ejes
ax.set_xlabel('x1')
ax.set_ylabel('x3')
ax.set_zlabel('x2')

# Leyenda de cada plano
r = mpatches.Patch(color='red', label='x1 + x2 + x3 + x4 = 10')
b = mpatches.Patch(color='blue', label='1.01x1 + 1.02x2 + ... = 20')
g = mpatches.Patch(color='green', label='cuadrados = 30')
p = mpatches.Patch(color='purple', label='cubos = 40')

ax.legend(handles=[r, b, g, p])

plt.title("Sistema (b)")
plt.tight_layout()
plt.show()
