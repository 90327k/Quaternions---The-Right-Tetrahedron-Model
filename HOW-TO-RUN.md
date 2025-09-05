# How to Run the Project & Visualizations

Follow these steps to get the Quaternion visualizations running on your computer.

## 1. Prerequisites

You need to have **Python 3** installed. You can download it from [python.org](https://www.python.org/downloads/).

*   **Important:** During installation, check the box that says **"Add Python to PATH"**.

## 2. Get the Code

Download this repository. You can click the green "Code" button and select "Download ZIP", or clone it using Git:
```bash
git clone https://github.com/your-username/Quaternions---The-Right-Tetrahedron-Model.git
```

## 3. Install the Dependencies

This project uses two main Python libraries: `numpy` and `matplotlib`.

**Open a terminal (Command Prompt, PowerShell, or shell) and navigate to the project folder.** Then, run the following command to install them:

```bash
pip install -r requirements.txt
```

*(If you have both Python 2 and 3, you might need to use `pip3` instead of `pip`).*

## 4. Explore and Run the Scripts

This project contains several Python scripts (`.py` files). Each one generates a different visualization.

**How to run any script:**
```bash
python name_of_the_script.py
```

### What to Look For and Run:

1.  **Look for a file** that might be named like:
    *   `plot_tetrahedron.py`
    *   `visualize.py`
    *   `generate_plots.py`
    *   `main.py`

2.  **Run it** with the command above. A window should open with a 3D plot.
    *   *You can usually rotate the 3D view by clicking and dragging with your mouse.*

3.  **Look for an animation script.** This is the most exciting part! The filename might be:
    *   `animate.py`
    *   `animation.py`
    *   `rotate_star.py`
    *   `quaternion_animation.py`

4.  **Run the animation script.** This will show the rotating Quaternion Star.
    *   *If the animation window is slow or unresponsive, try minimizing other applications.*

## Need Help? Common Fixes:

*   **`python` is not recognized:** Reinstall Python and ensure "Add to PATH" is checked.
*   **`pip` is not recognized:** Try using `pip3` or restart your terminal after installing Python.
*   **Animation doesn't show up:** Some environments work better with an alternative to `plt.show()`. Try changing the last line of the script to:
    ```python
    plt.show(block=True)  # Replace plt.show() with this
    ```
*   **Still stuck?** You can view the pre-generated visualizations (like the YouTube video) included in the README to understand the concepts.

## License

This visualization model was created by Mueed Malik (2025). It is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).
