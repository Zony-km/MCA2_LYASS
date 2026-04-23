import numpy as np
import matplotlib.pyplot as plt

# Definimos el rango de valores para la variable independiente x
x = np.linspace(0, 5, 400)

# Cálculo explícito de y para cada ecuación del sistema:
#   Ecuación 1:  x + 2y = 3           →  y = (3 - x) / 2
#   Ecuación 2:  2x + 4.0001y = 6.0001 → y = (6.0001 - 2x) / 4.0001
# Estas dos rectas son casi paralelas, lo que permite visualizar la
# sensibilidad del sistema ante perturbaciones mínimas.
y1 = (3 - x) / 2
y2 = (6.0001 - 2 * x) / 4.0001

# Configuración de la figura para la visualización
plt.figure(figsize=(10, 6))

# Representación gráfica de ambas rectas
plt.plot(x, y1, label='x + 2y = 3', color='blue', linewidth=2)
plt.plot(x, y2, label='2x + 4.0001y = 6.0001', color='red',
         linestyle='--', linewidth=2)

# Etiquetas y elementos visuales de referencia
plt.title('Sistema de Ecuaciones (c) - Rectas casi coincidentes')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)  # Eje horizontal
plt.axvline(0, color='black', linewidth=0.5)  # Eje vertical
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()

# Mostrar la gráfica resultante
plt.show()
