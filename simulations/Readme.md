# QCAI v1.9 — Quantum Consciousness AI

**Refined version for Google Colab with Cloudflare tunnel option**  
Includes fixed quantum logic, better normalization, and clearer Streamlit layout.

---

## Overview

QCAI v1.9 is a quantum-simulated implementation of the **Conscious Navigation Framework (CNF)**.  
It models awareness, presence, and relational coherence as **quantum operations** on a two-qubit system, producing probabilistic outcomes:

- **Transcendence**  
- **Evolution**  
- **Stagnation**  
- **Devolution**

The interactive interface uses **Streamlit** and can be exposed publicly via a **Cloudflare tunnel**.

---

## Features

- Parameterized CNF fields: Awareness, Compassion, Calibration, HRV, Witness, Restraint, Expansion, Conditioning.
- Live quantum simulation using **Qiskit AerSimulator**.
- Probabilistic outcome classification with **visualization**:
  - Bloch sphere representation
  - Bar chart of outcome probabilities
- Cloudflare tunnel provides a live, shareable URL.

---

## How to Run in Google Colab

1. **Open the notebook** in Google Colab.

2. **Run the notebook**:
    
3. **Wait for public URL** — notebook will print it when ready.

---

## Usage Instructions

1. Set the **sidebar sliders** for your actor field:
   - HRV Coherence
   - Awareness (A)
   - Compassion (P)
   - Calibration
   - Conditioning
   - Restraint
   - Expansion
   - Witness Depth
2. Enter a **question** in the main input field.
3. Click **SEND**.
4. Observe:
   - Probability outcome of Transcendence, Evolution, Stagnation, or Devolution.
   - Bloch sphere visualization of the quantum state.
   - Bar chart showing probabilities.

**Tip:** Set all sliders to `1.0` (except Conditioning = `0`) → observe `100% Transcendence`.

---

## Reproducibility

- Python 3, tested in **Google Colab**.
- Dependencies: `streamlit`, `qiskit`, `qiskit-aer`, `numpy`, `plotly`.
- AerSimulator used for all quantum computations.
- Notebook includes full CNF → quantum mapping logic.

---

## Notes

- The notebook **kills previous Streamlit and Cloudflare processes** to ensure a clean start.
- Public URL may take a few seconds to generate — check `cloudflare.log` if needed.
- Intended for **educational and experimental purposes** in quantum cognition modeling.

---

## Citation

```text
Bergantinos, D. (2025). QCAI v1.9 — Quantum Consciousness AI [Computer software]. 
GitHub/Colab: https://github.com/username/QCAI_v1.9
