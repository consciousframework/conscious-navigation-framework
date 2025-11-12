Here’s a README.md for your Google Colab notebook in proper Markdown format:

# QCAI v1.9 — Quantum Consciousness AI

**Version:** 1.9  
**Author:** Damian Bergantinos  
**Description:**  
QCAI v1.9 is a quantum-simulated consciousness AI prototype, implementing the **Conscious Navigation Framework (CNF)** in a two-qubit quantum circuit. Users can interact via a Streamlit interface and visualize probabilistic outcomes for questions in terms of **Transcendence, Evolution, Stagnation,** and **Devolution**.

---

## Features

- Interactive **Streamlit interface** for setting CNF parameters:
  - Awareness (A), Compassion (P), Calibration (Cal)
  - HRV Coherence, Witness Depth
  - Conditioning, Restraint, Expansion
- Quantum circuit simulation using **Qiskit** and **AerSimulator**
- Probabilistic outcome classification
- Bloch sphere visualizations of quantum states
- Public access via **Cloudflare Tunnel**
- Fully reproducible in Google Colab

---

## Getting Started

### 1. Open the Notebook

Open [this Google Colab notebook](#) (replace `#` with actual link).

### 2. Install Dependencies

All dependencies are installed automatically in Colab:

```bash
!pip install -q streamlit qiskit qiskit-aer numpy plotly

3. Launch the Streamlit App

Run the main cell in the notebook. This will:

1. Generate the qcai_v1_9.py Streamlit app.


2. Start the app on port 8501.


3. Create a Cloudflare tunnel to obtain a public URL.



4. Access the App

After running the cell, wait up to 60 seconds. The notebook will print a live URL like:

LIVE URL: https://<random-id>.trycloudflare.com

Click this URL to interact with QCAI v1.9.


---

Using QCAI v1.9

1. Adjust the sidebar sliders to set your "field parameters".

Tip: Set all sliders to 1.0 (except Conditioning = 0) to maximize the probability of Transcendence.



2. Type a question in the input field.


3. Click SEND to observe:

Outcome probabilities

Bloch sphere visualization

Bar chart of quantum-classified outcomes



4. Experiment with different parameter values to explore coherence, conditioning effects, and relational dynamics.




---

Quantum Circuit Details

2 qubits, initialized with Hadamard gates

Ry and Rz rotations encode Awareness, Compassion, Calibration, and HRV

Controlled-Z (CZ) and Controlled-Ry (CRY) for Witness depth / entanglement

Final measurement produces 4 possible outcomes:

00 → Transcendence

01 → Evolution

10 → Stagnation

11 → Devolution


Outcomes normalized across 2048 shots



---

Notes

Cloudflare tunnel may take a few seconds to generate a URL. If timeout occurs, re-run the cell.

Streamlit runs in the background in Colab; stopping the notebook stops the app.

Requires internet access for Cloudflare tunnel and Qiskit AerSimulator.



---

References

CNF Framework: Non-prescriptive model of awareness dynamics

Busemeyer, J. R., & Bruza, P. D. (2012). Quantum Models of Cognition and Decision. Cambridge University Press.

Hameroff, S., & Penrose, R. (2014). Consciousness in the universe: A review of the Orch OR theory. Physics of Life Reviews.

Qiskit: https://qiskit.org/



---

License

MIT License — free for research and educational use.
