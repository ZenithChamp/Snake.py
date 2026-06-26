# Asynchronous Matrix-Mapped Terminal Snake Engine

A real-time, non-blocking arcade Snake application built completely from scratch in Python. The system utilizes background operating system keyboard listeners, dynamic frame-flushing, and a structural vector queue to simulate organic movement updates over a 9x9 matrix without freezing execution loops.

## 🚀 Key Features
- **Asynchronous Execution Clock:** Integrates native `msvcrt` hardware intercepts to continuously stream frame updates and directional shifts without blocking the runtime cycle.
- **Continuous Boundary Wrapping:** Tracks mathematical index boundaries, automatically snapping coordinate matrices across border frames (`0` to `8`) for continuous gameplay.
- **Dynamic Trail Frame-Wiping:** Implements deep memory coordinate snapshots (`ot`) to actively flush old cell allocations back to empty spaces, preventing trail bleeding.
- **Dual-Condition Apple Core:** Computes apple point generation under a strict race condition—refreshing the grid position instantly if eaten by the head `h` or if a 20-second backend clock (`ac`) expires.

## 🛠️ Tech Stack & Concepts Used
- **Language:** Python 3
- **Libraries Used:** `tabulate`, `msvcrt` (Windows Input), `time`, `random`, `os`, `sys`
- **Concepts:** Linear Data Structure Simulation, Memory Pointer Scoping, State Cascading Loops.

## 💻 How to Run Locally

1. Install the tabular visualization package:
   ```bash
   pip install tabulate
   ```
2. Launch the application:
   ```bash
   python snake.py
   ```
3. Use keys `1` (Left), `2` (Up), `3` (Right), and `4` (Down) to change vectors on the fly!
