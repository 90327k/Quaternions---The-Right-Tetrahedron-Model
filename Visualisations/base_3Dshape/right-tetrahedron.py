import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def create_right_tetrahedron():
    # Define the vertices of the right tetrahedron
    # Origin point where all three right triangles meet
    origin = np.array([0, 0, 0])
    
    # Points along each axis
    x_point = np.array([1, 0, 0])
    y_point = np.array([0, 1, 0])
    z_point = np.array([0, 0, 1])
    
    return origin, x_point, y_point, z_point

def plot_right_triangles(ax, origin, x_point, y_point, z_point):
    # Plot the three right-angled triangles
    triangles = [
        [origin, x_point, y_point],  # XY plane triangle
        [origin, y_point, z_point],  # YZ plane triangle
        [origin, z_point, x_point]   # ZX plane triangle
    ]
    
    colors = ['red', 'green', 'blue']
    labels = ['XY Plane', 'YZ Plane', 'ZX Plane']
    
    for i, triangle in enumerate(triangles):
        verts = [list(triangle)]
        ax.add_collection3d(Poly3DCollection(verts, alpha=0.3, linewidths=1, edgecolors='black', facecolors=colors[i]))
    
    # Plot the points
    points = np.array([origin, x_point, y_point, z_point])
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], color='black', s=50)
    
    # Label the points
    ax.text(origin[0], origin[1], origin[2], 'O', fontsize=12, color='black')
    ax.text(x_point[0], x_point[1], x_point[2], 'X', fontsize=12, color='black')
    ax.text(y_point[0], y_point[1], y_point[2], 'Y', fontsize=12, color='black')
    ax.text(z_point[0], z_point[1], z_point[2], 'Z', fontsize=12, color='black')
    
    # Set labels and limits
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_zlim([0, 1])
    ax.set_title('Three Right-Angled Triangles Meeting at Origin')

def plot_complete_tetrahedron(ax, origin, x_point, y_point, z_point):
    # Plot the complete tetrahedron
    triangles = [
        [origin, x_point, y_point],
        [origin, y_point, z_point],
        [origin, z_point, x_point],
        [x_point, y_point, z_point]  # The hypotenuse face
    ]
    
    colors = ['red', 'green', 'blue', 'purple']
    
    for i, triangle in enumerate(triangles):
        verts = [list(triangle)]
        ax.add_collection3d(Poly3DCollection(verts, alpha=0.3, linewidths=1, edgecolors='black', facecolors=colors[i]))
    
    # Plot the points
    points = np.array([origin, x_point, y_point, z_point])
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], color='black', s=50)
    
    # Label the points
    ax.text(origin[0], origin[1], origin[2], 'O', fontsize=12, color='black')
    ax.text(x_point[0], x_point[1], x_point[2], 'X', fontsize=12, color='black')
    ax.text(y_point[0], y_point[1], y_point[2], 'Y', fontsize=12, color='black')
    ax.text(z_point[0], z_point[1], z_point[2], 'Z', fontsize=12, color='black')
    
    # Set labels and limits
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_zlim([0, 1])
    ax.set_title('Complete Right Tetrahedron')

# Create the figure with two subplots
fig = plt.figure(figsize=(12, 6))

# First subplot: Three right triangles
ax1 = fig.add_subplot(121, projection='3d')
origin, x_point, y_point, z_point = create_right_tetrahedron()
plot_right_triangles(ax1, origin, x_point, y_point, z_point)

# Second subplot: Complete tetrahedron
ax2 = fig.add_subplot(122, projection='3d')
plot_complete_tetrahedron(ax2, origin, x_point, y_point, z_point)

plt.tight_layout()
plt.show()
