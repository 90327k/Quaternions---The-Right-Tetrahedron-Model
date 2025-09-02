# The Right Tetrahedron Model of Quaternion Visualisation

Quaternions are often taught in a way that makes them seem abstract and overcomplicated.  
This project introduces a new **geometric model** — the **Right Tetrahedron Model** — that simplifies quaternion visualisation and makes their structure more intuitive.

---

## 🚀 Why This Matters
- Traditional teaching relies heavily on algebra, which hides the geometric simplicity of quaternions.
- This model uses the **right tetrahedron** as the base shape to visualise quaternion components.
- When four right tetrahedra are joined, they form a cube — representing the natural bounds of quaternion rotations.
- The **scalar part (w)** acts as the *anchor of rotation* (rotation density), while **x, y, z** describe vector directions.

> Quaternions are not 4D. They do however: use the 4th D to describe the 3rd D.  

---

## 🌀 Core Idea
- **Base unit:** A single right tetrahedron, with edges corresponding to `i, j, k`.
- **Pivot point (w):** Acts as the scalar anchor of rotation (±180°).
- **Cube bounds:** Four tetrahedra form a cube, visualising the limits of quaternion space.
- **Hypersphere analogy:** The full quaternion field can be seen as a 4D hypersphere, with `w` as rotation density and `xyz` as vector directions.

---

## 📷 Visualisations
### 1. Base Right Tetrahedron
![Base Tetrahedron](media/tetrahedron.png)

### 2. Quaternion Bounds
![Quaternion Bounds](media/cube_from_tetrahedra.png)

### 3. Rotating Around W
![Rotation](media/rotating_tetrahedron.gif)

All visualisations are generated using Python and `matplotlib`.



---

🔬 Explanation

A quaternion is written as: [ q = w + xi + yj + zk ]

In this model:

w = the pivot (rotation anchor, scalar part)

x, y, z = vector components (edges from w)


Rotations are described by: [ \cos(\theta/2) + \sin(\theta/2)(xi + yj + zk) ]

The tetrahedron visualises these relationships directly.



---


# License
This quaternion visualization model was created by Mueed Malik (2025).
It is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

If you use this work, please credit it as:
Mueed Malik, "The Right Tetrahedron Model of Quaternion Visualisation", 2025.
