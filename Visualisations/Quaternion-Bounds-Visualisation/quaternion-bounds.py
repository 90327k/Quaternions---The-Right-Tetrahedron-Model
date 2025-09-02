import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Set up the plot
fig = plt.figure(figsize=(20, 16))
fig.suptitle('Quaternion Bounds', 
             fontsize=18, fontweight='bold')

# Define parameters
L = 1  # Side length of legs

# Shared right-angle vertex
O = np.array([0, 0, 0])

# Define all 8 tetrahedra (one for each octant)
tetrahedra = {
    # Positive octant (XYZ)
    'T1': {
        'O': O,
        'A': np.array([L, 0, 0]),
        'B': np.array([0, L, 0]),
        'C': np.array([0, 0, L]),
        'color': 'lightcoral',
        'name': 'Positive XYZ'
    },
    # Negative X (Negative X, Positive YZ)
    'T2': {
        'O': O,
        'A': np.array([-L, 0, 0]),
        'B': np.array([0, L, 0]),
        'C': np.array([0, 0, L]),
        'color': 'lightblue',
        'name': 'Negative X'
    },
    # Negative Y (Positive X, Negative Y, Positive Z)
    'T3': {
        'O': O,
        'A': np.array([L, 0, 0]),
        'B': np.array([0, -L, 0]),
        'C': np.array([0, 0, L]),
        'color': 'lightgreen',
        'name': 'Negative Y'
    },
    # Negative Z (Positive XY, Negative Z)
    'T4': {
        'O': O,
        'A': np.array([L, 0, 0]),
        'B': np.array([0, L, 0]),
        'C': np.array([0, 0, -L]),
        'color': 'lightyellow',
        'name': 'Negative Z'
    },
    # Negative XY (Positive Z)
    'T5': {
        'O': O,
        'A': np.array([-L, 0, 0]),
        'B': np.array([0, -L, 0]),
        'C': np.array([0, 0, L]),
        'color': 'lightpink',
        'name': 'Negative XY'
    },
    # Negative XZ (Positive Y)
    'T6': {
        'O': O,
        'A': np.array([-L, 0, 0]),
        'B': np.array([0, L, 0]),
        'C': np.array([0, 0, -L]),
        'color': 'lightcyan',
        'name': 'Negative XZ'
    },
    # Negative YZ (Positive X)
    'T7': {
        'O': O,
        'A': np.array([L, 0, 0]),
        'B': np.array([0, -L, 0]),
        'C': np.array([0, 0, -L]),
        'color': 'lavender',
        'name': 'Negative YZ'
    },
    # Negative octant (Negative XYZ)
    'T8': {
        'O': O,
        'A': np.array([-L, 0, 0]),
        'B': np.array([0, -L, 0]),
        'C': np.array([0, 0, -L]),
        'color': 'wheat',
        'name': 'Negative XYZ'
    }
}

# Create a function to plot a tetrahedron
def plot_tetrahedron(ax, vertices, color, alpha=0.8):
    faces = [
        [vertices['O'], vertices['A'], vertices['B']],
        [vertices['O'], vertices['A'], vertices['C']],
        [vertices['O'], vertices['B'], vertices['C']],
        [vertices['A'], vertices['B'], vertices['C']]
    ]
    collection = Poly3DCollection(faces, alpha=alpha, linewidths=1.5, edgecolors='black')
    collection.set_facecolor(color)
    ax.add_collection3d(collection)

# Plot 1: All 8 tetrahedra overview
ax1 = fig.add_subplot(221, projection='3d')
for tetra_id, tetra in tetrahedra.items():
    plot_tetrahedron(ax1, tetra, tetra['color'], 0.6)
ax1.set_title('1. All 8 Tetrahedra (Overview)')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_xlim(-L-0.2, L+0.2)
ax1.set_ylim(-L-0.2, L+0.2)
ax1.set_zlim(-L-0.2, L+0.2)

# Highlight shared vertex O
ax1.scatter(*O, color='red', s=200, marker='o', edgecolors='black')
ax1.text(O[0], O[1], O[2], ' O ', fontsize=12, color='red', weight='bold')

# Plot 2: Positive octants (T1-T4)
ax2 = fig.add_subplot(222, projection='3d')
for tetra_id in ['T1', 'T2', 'T3', 'T4']:
    tetra = tetrahedra[tetra_id]
    plot_tetrahedron(ax2, tetra, tetra['color'], 0.8)
ax2.set_title('2. Tetrahedra with Positive Z Component')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_xlim(-L-0.2, L+0.2)
ax2.set_ylim(-L-0.2, L+0.2)
ax2.set_zlim(-L-0.2, L+0.2)
ax2.scatter(*O, color='red', s=150, marker='o')

# Plot 3: Negative octants (T5-T8)
ax3 = fig.add_subplot(223, projection='3d')
for tetra_id in ['T5', 'T6', 'T7', 'T8']:
    tetra = tetrahedra[tetra_id]
    plot_tetrahedron(ax3, tetra, tetra['color'], 0.8)
ax3.set_title('3. Tetrahedra with Negative Z Component')
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z')
ax3.set_xlim(-L-0.2, L+0.2)
ax3.set_ylim(-L-0.2, L+0.2)
ax3.set_zlim(-L-0.2, L+0.2)
ax3.scatter(*O, color='red', s=150, marker='o')

# Plot 4: Orthogonal view showing coordinate system
ax4 = fig.add_subplot(224, projection='3d')
for tetra_id, tetra in tetrahedra.items():
    plot_tetrahedron(ax4, tetra, tetra['color'], 0.4)
ax4.set_title('4. Coordinate System View')
ax4.set_xlabel('X')
ax4.set_ylabel('Y')
ax4.set_zlabel('Z')
ax4.set_xlim(-L-0.2, L+0.2)
ax4.set_ylim(-L-0.2, L+0.2)
ax4.set_zlim(-L-0.2, L+0.2)

# Draw coordinate axes
ax4.plot([-L, L], [0, 0], [0, 0], 'r-', linewidth=3, label='X-axis')
ax4.plot([0, 0], [-L, L], [0, 0], 'g-', linewidth=3, label='Y-axis')
ax4.plot([0, 0], [0, 0], [-L, L], 'b-', linewidth=3, label='Z-axis')

# Highlight shared vertex O
ax4.scatter(*O, color='red', s=250, marker='o', edgecolors='black')
ax4.text(O[0], O[1], O[2], ' ', 
         fontsize=11, color='red', weight='bold')

plt.tight_layout()
plt.show()

# Print detailed information
print("=" * 50)
print(f"Leg length (L): {L}")
print(f"Shared vertex O: {O}")
print(f"Each tetrahedron has 3 right triangles (legs = {L}) + 1 equilateral face (side = {L*np.sqrt(2):.3f})")

print("\nOctant Coverage:")
print("T1: Positive XYZ  (X+, Y+, Z+)")
print("T2: Negative X    (X-, Y+, Z+)")
print("T3: Negative Y    (X+, Y-, Z+)")
print("T4: Negative Z    (X+, Y+, Z-)")
print("T5: Negative XY   (X-, Y-, Z+)")
print("T6: Negative XZ   (X-, Y+, Z-)")
print("T7: Negative YZ   (X+, Y-, Z-)")
print("T8: Negative XYZ  (X-, Y-, Z-)")

print(f"\nVerification - All edges from O have length {L}:")
for tetra_id, tetra in tetrahedra.items():
    for vertex in ['A', 'B', 'C']:
        distance = np.linalg.norm(tetra[vertex] - O)
        print(f"  {tetra_id} O to {vertex}: {distance:.3f}")

print(f"\nTotal volume occupied: Cube from (-{L},-{L},-{L}) to ({L},{L},{L})")
