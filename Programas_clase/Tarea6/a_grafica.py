import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Visualización de tres planos en 3D

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(projection='3d')

# Rango de valores para generar (X, Y)
x = np.linspace(-1, 1, 50)
y = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(x, y)

# Definición de los planos:
#   Plano 1:  x + 1/2 y + 1/2 z = 1
#   Plano 2:  1/2 x + 1/3 y + 1/4 z = 0
#   Plano 3:  1/3 x + 1/4 y + 1/5 z = 0
# Cada expresión corresponde a z despejada.
Z1 = 2 * (1 - X - (1/2) * Y)
Z2 = 4 * (-(1/2) * X - (1/3) * Y)
Z3 = 5 * (-(1/3) * X - (1/4) * Y)

# Superficies de los planos
ax.plot_surface(X, Y, Z1, alpha=0.4, color='red', edgecolor='none')
ax.plot_surface(X, Y, Z2, alpha=0.4, color='blue', edgecolor='none')
ax.plot_surface(X, Y, Z3, alpha=0.4, color='green', edgecolor='none')

# Ajuste de la vista 3D
ax.view_init(elev=30, azim=135)

# Etiquetas de ejes
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Leyenda asociada a cada plano
rojo = mpatches.Patch(color='red', label='x + 1/2 y + 1/2 z = 1')
azul = mpatches.Patch(color='blue', label='1/2 x + 1/3 y + 1/4 z = 0')
verde = mpatches.Patch(color='green', label='1/3 x + 1/4 y + 1/5 z = 0')
ax.legend(handles=[rojo, azul, verde])

plt.title("Sistema (a)")
plt.tight_layout()
plt.show()
