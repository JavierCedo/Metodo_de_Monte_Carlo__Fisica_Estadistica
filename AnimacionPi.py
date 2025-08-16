import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def monte_carlo_pi_animation(num_puntos, save_as=None):
    
    # Configuración inicial de la figura
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_aspect('equal')
    ax.set_title('Estimación de Pi')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    
    # Dibujar el círculo de referencia
    circle = plt.Circle((0, 0), 1, color='green', fill=False, linestyle='--')
    ax.add_patch(circle)
    
    # Inicializar elementos de la animación
    scat = ax.scatter([], [], s=5)
    text = ax.text(0.05, 1.05, '', transform=ax.transAxes)
    
    # Listas para almacenar los puntos
    puntos_x = []
    puntos_y = []
    colores = []
    puntos_en_circulo = 0
    
    def init():
        scat.set_offsets(np.empty((0, 2)))
        text.set_text('')
        return scat, text
    
    def update(frame):
        nonlocal puntos_en_circulo
        
        # Generar un nuevo punto aleatorio
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distancia = (x**2 + y**2)**0.5
        
        # Determinar si está dentro del círculo
        if distancia <= 1:
            puntos_en_circulo += 1
            color = 'blue'
        else:
            color = 'red'
        
        # Agregar el punto a las listas
        puntos_x.append(x)
        puntos_y.append(y)
        colores.append(color)
        
        # Actualizar el gráfico de dispersión
        scat.set_offsets(np.column_stack((puntos_x, puntos_y)))
        scat.set_color(colores)
        
        # Calcular y mostrar la estimación actual de Pi
        pi_estimado = 4 * puntos_en_circulo / len(puntos_x)
        ax.set_title(f'Puntos: {len(puntos_x)}, Estimación de Pi: {pi_estimado:.5f}')
        
        return scat, text
    
    # Crear la animación
    ani = FuncAnimation(
        fig, update, frames=range(num_puntos),
        init_func=init, blit=True, interval=0.05, repeat=False
    )
    
    # Guardar la animación si se especificó un formato
    if save_as:
        if save_as.lower().endswith('.gif'):
            ani.save(save_as, writer='pillow', fps=30, dpi=100)
        elif save_as.lower().endswith('.mp4'):
            ani.save(save_as, writer='ffmpeg', fps=30, dpi=100)
        else:
            print("Formato no soportado. Usa .gif o .mp4")
    
    plt.tight_layout()
    plt.show()
    
    # Calcular el valor final de Pi
    pi_estimado = 4 * puntos_en_circulo / num_puntos
    return pi_estimado

# Uso del código
NumeroParticulas = 10000
pi_calculado = monte_carlo_pi_animation(NumeroParticulas, save_as='monte_carlo_pi.gif')
print(f"El valor estimado de Pi con {NumeroParticulas} puntos es: {pi_calculado}")