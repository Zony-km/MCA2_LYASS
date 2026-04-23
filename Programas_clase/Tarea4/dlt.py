import numpy as np

def calcular_proyeccion_dlt(puntos3D, puntos2D):
    """
    Calcula la matriz de proyección usando el método DLT.
    """
    sistema = []

    for idx in range(len(puntos3D)):
        Xw, Yw, Zw = puntos3D[idx]
        u_img, v_img = puntos2D[idx]

        # Ecuaciones lineales del sistema A * p = 0
        sistema.append([Xw, Yw, Zw, 1, 0, 0, 0, 0, -u_img*Xw, -u_img*Yw, -u_img*Zw, -u_img])
        sistema.append([0, 0, 0, 0, Xw, Yw, Zw, 1, -v_img*Xw, -v_img*Yw, -v_img*Zw, -v_img])

    sistema = np.asarray(sistema)

    # Resolver con SVD
    _, _, Vt = np.linalg.svd(sistema)
    P = Vt[-1].reshape(3, 4)

    # Normalizar si es posible
    if P[2, 3] != 0:
        P = P / P[2, 3]

    return P


# --- Datos del mundo real (3D) ---
coords_mundo = np.array([
    [0, 0, 0],
    [15, 0, 0],
    [0, 8, 0],
    [15, 8, 0],
    [0, 0, 3],
    [15, 8, 3]
])

# --- Datos en imagen (2D) ---
coords_imagen = np.array([
    [960, 800],
    [1400, 750],
    [960, 450],
    [1400, 400],
    [860, 850],
    [1300, 350]
])

# Calcular matriz de proyección
P = calcular_proyeccion_dlt(coords_mundo, coords_imagen)

print("-" * 40)
print(" MATRIZ DE PROYECCIÓN OBTENIDA (DLT) ")
print("-" * 40)
np.set_printoptions(suppress=True, precision=5)
print(P)
print("-" * 40)

# --- Verificación de reproyección ---
print("\nReproyección de puntos:")
for i in range(len(coords_mundo)):
    punto_h = np.append(coords_mundo[i], 1)
    reproy = P @ punto_h

    w = reproy[2]
    u_est = reproy[0] / w
    v_est = reproy[1] / w

    error = np.sqrt((u_est - coords_imagen[i][0])**2 + (v_est - coords_imagen[i][1])**2)

    print(f"P{i+1}: Real ({coords_imagen[i][0]}, {coords_imagen[i][1]}) -> "
          f"Calc ({u_est:.1f}, {v_est:.1f}) | Error: {error:.2f} px")
