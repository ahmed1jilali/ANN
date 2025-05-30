import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def cost_function(w1, w2,
                  base=0.5,
                  A_global=0.45,   # base − A_global = 0.05
                  A_local= 0.35,   # base − A_local  = 0.15
                  A_peak=  0.30,   # base + A_peak  = 0.80
                  A_bump1= 0.10,   # base + A_bumpX = 0.60
                  A_bump2= 0.10,
                  A_bump3= 0.10):
    # Global minimum dip at (0.7,0.4)
    gm = -A_global * np.exp(-((w1 - 0.7)**2 + (w2 - 0.4)**2) / 0.01)
    # Local minimum dip at (0.2,0.7)
    lm = -A_local  * np.exp(-((w1 - 0.2)**2 + (w2 - 0.7)**2) / 0.02)
    # Peak at (0.4,0.6)
    pk =  A_peak  * np.exp(-((w1 - 0.4)**2 + (w2 - 0.6)**2) / 0.015)
    # Bumps
    b1 = A_bump1 * np.exp(-((w1 - 0.3)**2 + (w2 - 0.2)**2) / 0.005)
    b2 = A_bump2 * np.exp(-((w1 - 0.8)**2 + (w2 - 0.8)**2) / 0.005)
    b3 = A_bump3 * np.exp(-((w1 - 0.5)**2 + (w2 - 0.1)**2) / 0.005)

    return base + gm + lm + pk + b1 + b2 + b3

# Create a fine grid
w1 = np.linspace(0, 1, 200)
w2 = np.linspace(0, 1, 200)
W1, W2 = np.meshgrid(w1, w2)
J  = cost_function(W1, W2)

# Plotting
fig = plt.figure(figsize=(10, 7))
ax  = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(W1, W2, J,
                       cmap='viridis',
                       edgecolor='k',
                       linewidth=0.2,
                       antialiased=True,
                       alpha=0.9)

# Annotations for the key points
pts = {
    'Global min': ((0.7, 0.4),  cost_function(0.7, 0.4)),
    'Local min' : ((0.2, 0.7),  cost_function(0.2, 0.7)),
    'Peak'      : ((0.4, 0.6),  cost_function(0.4, 0.6))
}
max_z = J.max()
for label, ((x,y), z) in pts.items():
    ax.scatter(x, y, z, s=50, color='r')
    #ax.text(x, y, max_z + 0.05, label, fontsize=9, ha='center', color='red')

# Axis labels & limits
ax.set_xlabel('$w_1$', labelpad=10)
ax.set_ylabel('$w_2$', labelpad=10)
ax.set_zlabel('$E$',   labelpad=10)
ax.set_zlim(0, 1)

# Nice view angle
ax.view_init(elev=35, azim=-60)

fig.colorbar(surf, shrink=0.5, aspect=10)
plt.tight_layout()
plt.show()
