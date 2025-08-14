import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 500)
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

plt.figure(figsize=(6, 6))
for i in range(1, len(t)):
    plt.plot(x[:i], y[:i], color='red')
    plt.pause(0.01)  

plt.text(0, 0, 'Panadda', fontsize=24, color='magenta', ha='center', va='center', fontweight='bold')

plt.axis('equal')
plt.axis('off')
plt.show()