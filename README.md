# The Right Tetrahedron Model of Quaternion Visualisation

Quaternions are often taught in a way that makes them seem abstract and overcomplicated.  
This project introduces a new **geometric model** — the **Right Tetrahedron Model** — that simplifies quaternion visualisation and makes their structure more intuitive.

---

# Why This Matters

- Traditional teaching relies heavily on algebra, which hides the geometric simplicity of quaternions.
- This model uses the **right tetrahedron** as the base shape to visualise quaternion components.
- When eight tetrahedra are joined at a common pivot, they form the Quaternion Star — a geometric representation of the natural bounds of quaternion rotations.
- The **scalar part (w)** acts as the *anchor of rotation* (rotation density), while **x, y, z** describe vector directions.

> Quaternions are thought to be 4D. In reality, they simply use four dimensions to describe the third dimension.  

---

# Core 

- **Base unit:** A single right tetrahedron, with edges corresponding to `i, j, k`.
- **Pivot point (w):** Acts as the scalar anchor of rotation (±180°).
- **Quaternion bounds:** Eight tetrahedra conjoined at `w` , visualising the limits of quaternion space.
- **Hypersphere analogy:** The full quaternion field can be seen as a 4D hypersphere, with `w` as rotation density and `xyz` as vector directions.

---

# The Visualisation Triad of Quaternion Fluency

### 1. Base Right Tetrahedron
<img width="637" height="519" alt="image" src="https://github.com/user-attachments/assets/4f6155d6-4559-46e5-a279-f3ca078e2622" />



### 2. Quaternion Bounds / The Quaternion Star
<img width="516" height="488" alt="image" src="https://github.com/user-attachments/assets/c65ed8d5-2b1b-4500-9189-0a4912cf4af5" />


### Rotating Around W

https://youtu.be/EumXnFZXhr4?si=hVrWm-AxOX7mnUb0

All visualisations are generated using Python and `matplotlib`.

### The Quaternion Hypersphere



---
# Explanation

A quaternion is written as: `[ q = w + xi + yj + zk ]`

In this model:

`w` = the pivot (rotation anchor, scalar part)

`x, y, z` = real vector components (real edges from w)

`i, j, k` = imaginary vector components (imaginary edges from w)

Rotations are described by: `[ \cos(\theta/2) + \sin(\theta/2)(xi + yj + zk) ]`

The tetrahedron visualises these relationships directly.


---


# License
This quaternion visualization model was created by Mueed Malik (2025).
It is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

If you use this work, please credit it as:
Mueed Malik, "The Right Tetrahedron Model of Quaternion Visualisation", 2025.
