import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import imageio
from PIL import Image

# Simulate molecular orbital
x = np.linspace(-3, 3, 30)
y = np.linspace(-3, 3, 30)
X, Y = np.meshgrid(x, y)
Z = np.exp(-X**2 - Y**2) * np.sin(X) * np.cos(Y)  # some pattern

frames = []
for angle in range(0, 360, 15):
    fig = plt.figure(figsize=(4,4))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    ax.view_init(elev=30, azim=angle)
    ax.set_axis_off()
    fig.tight_layout()
    fig.canvas.draw()
    buf = fig.canvas.tostring_argb()
    ncols, nrows = fig.canvas.get_width_height()
    img = Image.frombuffer('RGBA', (ncols, nrows), buf, 'raw', 'RGBA', 0, 1)
    img = img.convert('RGB')
    frames.append(np.array(img))
    plt.close(fig)

imageio.mimsave('orbital_3d.gif', frames, fps=10, loop=0)
print("3D orbital GIF saved.")
