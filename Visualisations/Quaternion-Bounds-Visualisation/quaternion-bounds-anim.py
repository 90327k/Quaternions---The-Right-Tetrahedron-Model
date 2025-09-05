import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation

# ==========================================
# Configuration
# ==========================================
SCALE = 1.0
COLORS = ['cyan', 'lightblue', 'lightgreen', 'lightsalmon',
          'lavender', 'lightpink', 'lightyellow', 'lightgray']

# ==========================================
# Quaternion Class (Unity-Compatible)
# ==========================================
class Quaternion:
    """Quaternion implementation compatible with Unity operations."""
    def __init__(self, w=1, x=0, y=0, z=0):
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, other):
        """Quaternion multiplication."""
        w = self.w * other.w - self.x * other.x - self.y * other.y - self.z * other.z
        x = self.w * other.x + self.x * other.w + self.y * other.z - self.z * other.y
        y = self.w * other.y - self.x * other.z + self.y * other.w + self.z * other.x
        z = self.w * other.z + self.x * other.y - self.y * other.x + self.z * other.w
        return Quaternion(w, x, y, z)

    def conjugate(self):
        return Quaternion(self.w, -self.x, -self.y, -self.z)

    def rotate_point(self, point):
        """Rotate a 3D point using this quaternion."""
        p = Quaternion(0, *point)
        rotated = self * p * self.conjugate()
        return np.array([rotated.x, rotated.y, rotated.z])

    @staticmethod
    def from_axis_angle(axis, angle):
        """Create quaternion from axis-angle representation."""
        axis = axis / np.linalg.norm(axis)
        half_angle = angle / 2.0
        s = np.sin(half_angle)
        return Quaternion(np.cos(half_angle), *(axis * s))

    def to_euler(self):
        """Convert quaternion to Euler angles (degrees)."""
        sinr_cosp = 2 * (self.w * self.x + self.y * self.z)
        cosr_cosp = 1 - 2 * (self.x**2 + self.y**2)
        roll = np.arctan2(sinr_cosp, cosr_cosp)

        sinp = 2 * (self.w * self.y - self.z * self.x)
        pitch = np.pi / 2 * np.sign(sinp) if abs(sinp) >= 1 else np.arcsin(sinp)

        siny_cosp = 2 * (self.w * self.z + self.x * self.y)
        cosy_cosp = 1 - 2 * (self.y**2 + self.z**2)
        yaw = np.arctan2(siny_cosp, cosy_cosp)

        return np.degrees(roll), np.degrees(pitch), np.degrees(yaw)

# ==========================================
# Geometry Helpers
# ==========================================
def tetrahedron_vertices(scale=SCALE):
    return np.array([[0, 0, 0], [scale, 0, 0], [0, scale, 0], [0, 0, scale]])

def tetrahedron_faces(vertices):
    return [[vertices[0], vertices[1], vertices[2]],
            [vertices[0], vertices[1], vertices[3]],
            [vertices[0], vertices[2], vertices[3]],
            [vertices[1], vertices[2], vertices[3]]]

def generate_quaternion_star(scale=SCALE):
    tetra_list = []
    for sx in [1, -1]:
        for sy in [1, -1]:
            for sz in [1, -1]:
                verts = tetrahedron_vertices(scale) * [sx, sy, sz]
                tetra_list.append(verts)
    return tetra_list

# ==========================================
# Plot Setup
# ==========================================
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(left=0.0, bottom=0.0, right=1.0, top=0.9)

ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1.5, 1.5])
ax.set_xlabel('X (i)')
ax.set_ylabel('Y (j)')
ax.set_zlabel('Z (k)')
ax.set_title('Right Tetrahedron Model of Quaternion Visualization', fontsize=14, pad=20)

# Add axes
ax.quiver(0, 0, 0, 1.5, 0, 0, color='r', arrow_length_ratio=0.1, label='X (i)')
ax.quiver(0, 0, 0, 0, 1.5, 0, color='g', arrow_length_ratio=0.1, label='Y (j)')
ax.quiver(0, 0, 0, 0, 0, 1.5, color='b', arrow_length_ratio=0.1, label='Z (k)')
ax.legend()

# Explanation text
explanation = (
    "Quaternion q = w + xi + yj + zk\n"
    "• W = scalar part (pivot point)\n"
    "• X, Y, Z = vector components\n"
    "• Each tetrahedron = one octant of quaternion space"
)
ax.text2D(0.05, 0.95, explanation, transform=ax.transAxes, fontsize=10,
          bbox=dict(boxstyle="round,pad=0.5", facecolor="lightyellow", alpha=0.7))

rotation_text = ax.text2D(0.05, 0.15, "", transform=ax.transAxes, fontsize=10,
                          bbox=dict(boxstyle="round,pad=0.5", facecolor="white", alpha=0.7))

# ==========================================
# Create Tetrahedra
# ==========================================
tetra_list = generate_quaternion_star(SCALE)
poly_collections = []
for i, verts in enumerate(tetra_list):
    faces = tetrahedron_faces(verts)
    poly3d = Poly3DCollection(faces, facecolors=COLORS[i % len(COLORS)], edgecolors='k', alpha=0.6)
    ax.add_collection3d(poly3d)
    poly_collections.append((verts, poly3d))

# ==========================================
# Rotation Sequence
# ==========================================
def create_rotation_sequence():
    time_points = np.linspace(0, 4 * np.pi, 200)
    rotations = []
    for t in time_points:
        axis = np.array([np.sin(t), np.cos(t * 0.7), np.sin(t * 0.3 + 1)])
        axis /= np.linalg.norm(axis)
        angle = np.radians(45 * np.sin(t * 0.5))
        rotations.append((axis, angle))
    return rotations

rotation_sequence = create_rotation_sequence()

# ==========================================
# Animation Update
# ==========================================
def update(frame):
    axis, angle = rotation_sequence[frame % len(rotation_sequence)]
    q = Quaternion.from_axis_angle(axis, angle)

    for i, (verts, poly3d) in enumerate(poly_collections):
        rotated_verts = np.array([q.rotate_point(v) for v in verts])
        poly3d.set_verts(tetrahedron_faces(rotated_verts))

    roll, pitch, yaw = q.to_euler()
    rotation_info = (f"Axis: ({axis[0]:.2f}, {axis[1]:.2f}, {axis[2]:.2f})\n"
                     f"Angle: {np.degrees(angle):.1f}°\n"
                     f"Quaternion: ({q.w:.2f}, {q.x:.2f}, {q.y:.2f}, {q.z:.2f})\n"
                     f"Euler: ({roll:.1f}, {pitch:.1f}, {yaw:.1f})")
    rotation_text.set_text(rotation_info)

    return [pc for _, pc in poly_collections] + [rotation_text]

# ==========================================
# Run Animation
# ==========================================
ani = FuncAnimation(fig, update, frames=len(rotation_sequence), interval=50, blit=False, repeat=True)

plt.figtext(0.5, 0.02,
            "Right Tetrahedron Model of Quaternion Visualization\nCreated by Mueed Malik (2025) - CC BY 4.0",
            ha="center", fontsize=9, bbox=dict(boxstyle="round,pad=0.5", facecolor="lightgray", alpha=0.7))

plt.show()
