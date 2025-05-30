import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data setup
x = np.arange(0, 1.1, 0.1)
y = np.arange(0, 1.1, 0.1)
X, Y = np.meshgrid(x, y)
Z = np.array([
    [.7,.6,.6,.5,.7,.4,.8,.3,.3,.3,.5],
    [.4,.4,.4,.4,.8,.5,.4,.2,.2,.2,.3],
    [.3,.3,.3,.3,.3,.5,.1,.1,.1,.2,.3],
    [.3,.2,.2,.2,.3,.4,.4, 0,.1,.2,.3],
    [.3,.2,.1,.2,.3,.2,.2,.3,.4,.7,.7],
    [.3,.2,.2,.2,.3,.5,.5,.5,.5,.4,.7],
    [.3,.3,.3,.3,.3,.2,.2,.2,.2,.4,.7],
    [.2,.2,.2,.3,.4,.4,.2,.1,.2,.4,.7],
    [.2,.3,.1,.3,.6,.6,.2,.2,.2,.4,.7],
    [.2,.3,.3,.3,.8,.8,.4,.4,.4,.5,.8],
    [.3,.5,.5,.5,.9,.9,.8,.6,.8,.8, 1]
])

# Create plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot surface
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.9)

# Labels and appearance
ax.set_title('Cost Function Surface of Neuron with Two Inputs')
ax.set_xlabel('$w_1$')
ax.set_ylabel('$w_2$')
ax.set_zlabel('Mean Squared Error')
ax.view_init(elev=30, azim=-60)  # camera view (like Plotly's camera_eye)

# Add colorbar
fig.colorbar(surf, shrink=0.5, aspect=10)

# Annotate global minimum (visually identified from Z array)
min_idx = np.unravel_index(np.argmin(Z), Z.shape)
global_min = (X[min_idx], Y[min_idx], Z[min_idx])
ax.scatter(*global_min, color='red', s=100, label='Global Minimum')
ax.legend()

plt.tight_layout()
plt.show()


















# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D        # registers the 3-D projection
# # Optional – for smoothing. Comment out both SciPy lines if you don’t need interpolation
# from scipy.interpolate import interp2d         

# # --------- 1.  GRID SETUP (small & editable) -----------------
# grid_size   = 5                    # 5 × 5 grid  → only 25 Z-values
# x = np.linspace(0, 1, grid_size)   # w1
# y = np.linspace(0, 1, grid_size)   # w2

# baseline    = 0.50                 # flat “table-top” value
# peak_val    = 1.00                 # tall error spike
# local_min   = 0.15                 # shallow dip
# global_min  = 0.00                 # deepest dip

# # Build Z as a mostly-flat array
# Z = np.full((grid_size, grid_size), baseline)

# # Coordinates for the three special points (row, col)
# peak_idx       = (3, 3)    # high error
# local_min_idx  = (1, 3)
# global_min_idx = (2, 2)

# Z[peak_idx]       = peak_val
# Z[local_min_idx]  = local_min
# Z[global_min_idx] = global_min

# # --------- 2.  (OPTIONAL) INTERPOLATE FOR A SMOOTH LOOK -------
# # Comment this block if you’re happy with a blockier surface
# f_interp = interp2d(x, y, Z, kind='cubic')
# x_fine   = np.linspace(0, 1, 100)
# y_fine   = np.linspace(0, 1, 100)
# X, Y     = np.meshgrid(x_fine, y_fine)
# Z_fine   = f_interp(x_fine, y_fine)
# # ----------------------------------------------------------------

# # --------- 3.  APPEARANCE VARIABLES YOU CAN TWEAK --------------
# cmap_color    = 'viridis'   # any Matplotlib colormap string
# surface_alpha = 0.9         # transparency (0.0 – 1.0)
# z_compression = 0.35        # 1 = normal height, <1 squashes Z axis
# # ----------------------------------------------------------------

# # --------- 4.  PLOT --------------------------------------------
# fig = plt.figure(figsize=(9, 6))
# ax  = fig.add_subplot(111, projection='3d')

# # Plot either the fine (smoothed) or coarse surface
# surf = ax.plot_surface(X, Y, Z_fine,             # <— use Z_fine for smooth
# # surf = ax.plot_surface(*np.meshgrid(x, y), Z,  # <— or swap to the coarse one
#                        cmap=cmap_color, alpha=surface_alpha,
#                        edgecolor='none')

# # Axis labels & view
# ax.set_title('Cost-function surface: mostly flat, one peak, two minima')
# ax.set_xlabel('$w_1$'); ax.set_ylabel('$w_2$'); ax.set_zlabel('Mean Squared Error')
# ax.view_init(elev=30, azim=-60)
# ax.set_box_aspect([1, 1, z_compression])         # compress Z-axis height

# # Highlight the three special points
# def scatter_point(idx, color, label):
#     ax.scatter(x[idx[1]], y[idx[0]], Z[idx], color=color, s=90, label=label)

# scatter_point(peak_idx,       'red', 'High error peak')
# scatter_point(local_min_idx,  'gold',    'Local minimum')
# scatter_point(global_min_idx, 'blue',    'Global minimum')
# ax.legend()

# fig.colorbar(surf, shrink=0.55, aspect=10)
# plt.tight_layout()
# plt.show()




