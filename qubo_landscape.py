import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import imageio
from PIL import Image

# Create a 2D energy landscape (simulated QUBO objective)
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = (X-0.5)**2 + (Y+0.3)**2 - 0.5*np.sin(3*X)*np.cos(3*Y)

frames = []
for t in np.linspace(0, 2*np.pi, 30):
    plt.figure(figsize=(4,4))
    Z_shifted = Z + 0.2*np.sin(t)
    plt.contourf(X, Y, Z_shifted, levels=20, cmap='coolwarm')
    plt.title("QUBO Energy Landscape")
    plt.xlabel("Variable 1")
    plt.ylabel("Variable 2")
    plt.tight_layout()
    plt.savefig("landscape_temp.png")
    img = imageio.imread("landscape_temp.png")
    frames.append(img)
    plt.close()

imageio.mimsave('qubo_landscape.gif', frames, fps=10, loop=0)
print("QUBO landscape GIF saved.")
