import numpy as np
import matplotlib.pyplot as plt

# Paramètres
C = 0.0                   # Seuil de la fonction indicatrice
k = 10.0                  # Raideur pour sigmoïde / tanh
epsilon = 0.5             # Largeur de transition pour rampe / cubique
x = np.linspace(-2, 2, 500)

# Fonction indicatrice (non Lipschitzienne)
indicator = (x >= C).astype(float)

# 1. Sigmoïde
sigmoid = 1 / (1 + np.exp(-k * (x - C)))

# 2. Tanh transformée
tanh_trans = 0.5 * (1 + np.tanh(k * (x - C)))

# 3. Rampe linéaire
ramp = np.piecewise(
    x,
    [x <= C - epsilon, (x > C - epsilon) & (x < C + epsilon), x >= C + epsilon],
    [0,
     lambda x: 0.5 / epsilon * (x - (C - epsilon)),
     1]
)

# 4. ReLU lissée équivalente (même que rampe ici, écriture différente)
relu_smooth = np.clip((x - (C - epsilon)) / (2 * epsilon), 0, 1)

# 5. Cubique (Hermite)
def cubic_transition(x, C, epsilon):
    t = (x - (C - epsilon)) / (2 * epsilon)
    t = np.clip(t, 0, 1)
    return 3 * t**2 - 2 * t**3

cubic = cubic_transition(x, C, epsilon)

# Affichage
plt.figure(figsize=(10, 6))
plt.plot(x, indicator, 'k--', label='Indicatrice (non Lipschitz)')
plt.plot(x, sigmoid, label='Sigmoïde')
plt.plot(x, tanh_trans, label='Tanh transformée')
plt.plot(x, ramp, label='Rampe')
plt.plot(x, relu_smooth, label='ReLU lissée')
plt.plot(x, cubic, label='Cubique (Hermite)')

plt.title('Approximations Lipschitziennes de la fonction indicatrice $1_{x \geq C}$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('plot_comparaison_fonctions.png')
