import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider

# Parâmetros da epicicloide
R = 4  # Raio da circunferência maior
r = 1  # Raio da circunferência menor

t = np.linspace(0, 2 * np.pi, 1000)
k = (R + r) / r  # Fator de multiplicação angular

# Equações da epicicloide
x = (R + r) * np.cos(t) - r * np.cos(k * t)
y = (R + r) * np.sin(t) - r * np.sin(k * t)

# Circunferência maior
theta = np.linspace(0, 2 * np.pi, 500)
xc = R * np.cos(theta)
yc = R * np.sin(theta)

# Estilo dos eixos 
def estilizar_axes(ax):
    ax.set_facecolor('#1e1e1e')
    ax.tick_params(colors='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.title.set_color('white')
    ax.grid(True, color='gray', linestyle='--', alpha=0.3)
    for spine in ax.spines.values():
        spine.set_color('white')

# Criação da figura 
fig, ax = plt.subplots(figsize=(8, 8), facecolor='#1e1e1e')
plt.subplots_adjust(bottom=0.25)

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
ax.set_title("ATV_03 - TEOREMA DE GREEN\nCURVA DA EPICICLOIDE\n", fontsize=14)
estilizar_axes(ax)

# Circunferência base
ax.plot(xc, yc, color='white', linestyle='--', linewidth=1.5, label='Circunferência maior (raio 4)')

# Elementos animados 
circ_menor, = ax.plot([], [], color='green', alpha=0.5, lw=1.5, label='Circunferência menor (raio 1)')
centro, = ax.plot([], [], 'o', color='green', markersize=4, label='Centro da menor circunferência')
ponto, = ax.plot([], [], 'o', color='white', markersize=6, label='Ponto P')
linha, = ax.plot([], [], color='cyan', lw=2, label='Epicicloide')

# Plotagem da legenda
circ_menor.set_data([0], [0])
centro.set_data([0], [0])
ponto.set_data([0], [0])
linha.set_data([0], [0])

# Configurações da legenda 
leg = plt.legend(
    facecolor='#1e1e1e',
    edgecolor='white',
    labelcolor='white',
    fontsize=8,
    loc='upper right',
    bbox_to_anchor=(1, 1),
    labelspacing=0.4
)
for text in leg.get_texts():
    text.set_color('white')

# Funções de animação 
def init():
    linha.set_data([], [])
    ponto.set_data([], [])
    circ_menor.set_data([], [])
    centro.set_data([], [])
    return linha, ponto, circ_menor, centro

def update(frame):
    linha.set_data(x[:frame], y[:frame])
    ponto.set_data(x[frame], y[frame])

    t_val = t[frame]
    cx = (R + r) * np.cos(t_val)
    cy = (R + r) * np.sin(t_val)
    centro.set_data(cx, cy)

    theta2 = np.linspace(0, 2 * np.pi, 100)
    rot_angle = -k * t_val

    xm = cx + r * np.cos(theta2 + rot_angle)
    ym = cy + r * np.sin(theta2 + rot_angle)
    circ_menor.set_data(xm, ym)

    return linha, ponto, circ_menor, centro

# Controle de velocidade
intervalo = [20]  # Intervalo base em milissegundos

ani = animation.FuncAnimation(
    fig, update, frames=range(0, len(t), 5),  # Avança 5 frames por vez → 5x mais rápido
    init_func=init, interval=intervalo[0], blit=True
)

# Slider de velocidade 
ax_slider = plt.axes([0.25, 0.1, 0.5, 0.03], facecolor='#333333')
slider = Slider(
    ax=ax_slider, label='Velocidade', 
    valmin=1, valmax=100, valinit=50, 
    color='lightgreen'
)

# Cores
slider.label.set_color('white')
slider.valtext.set_color('white')

# Função que altera a velocidade
intervalo_min = 2
intervalo_max = 100

def update_speed(val):
    intervalo_calc = intervalo_max - val + intervalo_min
    intervalo[0] = intervalo_calc
    ani.event_source.interval = intervalo_calc
    print(f'Velocidade slider: {val} -> Intervalo (ms): {intervalo_calc}')

slider.on_changed(update_speed)

plt.show()