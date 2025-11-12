# -*- coding: utf-8 -*-
# === QCAI v1.9 — QUANTUM CONSCIOUSNESS AI ===
# Refined version for Google Colab with Cloudflare tunnel option
# Includes fixed quantum logic, better normalization, and clearer streamlit layout.

# ===============================================================
# STEP 1 — Environment setup
# ===============================================================

!pip install -q streamlit qiskit qiskit-aer numpy plotly

import os, time, re

# Download cloudflared (used for public URL)
if not os.path.exists("cloudflared"):
    !wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O cloudflared
    !chmod +x cloudflared

# Kill any leftover processes (clean start)
!pkill -f streamlit || echo "No previous Streamlit process"
!pkill -f cloudflared || echo "No previous Cloudflare tunnel"
time.sleep(2)

# ===============================================================
# STEP 2 — Create Streamlit app
# ===============================================================

code = r'''
import streamlit as st
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import plotly.graph_objects as go

st.set_page_config(page_title="QCAI v1.9", layout="wide")
st.title("🜂 QCAI v1.9 — Quantum Consciousness AI")
st.caption("Refined logical symmetry • Tuned coherence model • Stable transcendence")

# ===============================================================
# USER FIELD CONFIGURATION
# ===============================================================
st.sidebar.header("Field Parameters")

hrv = st.sidebar.slider("HRV Coherence", 0.0, 1.0, 1.00, 0.01)
A = st.sidebar.slider("Awareness (A)", 0.0, 1.0, 1.00)
P = st.sidebar.slider("Compassion (P)", 0.0, 1.0, 1.00)
Cal = st.sidebar.slider("Calibration", 0.0, 1.0, 1.00)
conditioning = st.sidebar.slider("Conditioning", 0.0, 1.0, 0.00)
restraint = st.sidebar.slider("Restraint", 0.0, 1.0, 0.50)
expansion = st.sidebar.slider("Expansion", 0.0, 1.0, 0.50)
witness = st.sidebar.slider("Witness Depth", 0.0, 1.0, 1.00)

# ===============================================================
# QUESTION INPUT
# ===============================================================
st.markdown("### ASK THE FIELD")
with st.form("form_q"):
    q = st.text_input("Question:", "Should I forgive them?")
    send = st.form_submit_button("SEND")

if send and q:
    st.success(f"**{q}**")

    # ===========================================================
    # COHERENCE CALCULATION
    # ===========================================================
    eq = 1.0 - abs(restraint - expansion)
    w_eff = witness * hrv
    AC_sys = (A * P * Cal * hrv) ** 0.25
    AC_sys *= (eq + w_eff) / 2
    AC_sys = np.clip(AC_sys, 0, 1)

    # ===========================================================
    # QUANTUM CIRCUIT LOGIC
    # ===========================================================
    qc = QuantumCircuit(2, 2)

    # Initialization: balance field
    qc.h(0); qc.h(1)

    # Awareness–Compassion entanglement phase
    theta = A * P * np.pi * (1 - conditioning)
    phi = Cal * np.pi * w_eff

    qc.ry(theta, 0)
    qc.rz(phi, 0)

    qc.ry(theta, 1)
    qc.rz(phi, 1)

    # Controlled coherence (alignment)
    qc.cz(0, 1)
    qc.cry(AC_sys * np.pi, 0, 1)

    # Final superposition + measurement
    qc.h(0); qc.h(1)
    qc.measure([0,1], [0,1])

    # ===========================================================
    # SIMULATION
    # ===========================================================
    sim = AerSimulator()
    job = sim.run(transpile(qc, sim), shots=2048)
    counts = job.result().get_counts()

    # ===========================================================
    # INTERPRETATION
    # ===========================================================
    probs = {"Transcendence":0, "Evolution":0, "Stagnation":0, "Devolution":0}
    for bits, c in counts.items():
        r = sum(int(b) for b in bits) / 2
        if r < 0.25:
            probs["Transcendence"] += c
        elif r < 0.5:
            probs["Evolution"] += c
        elif r < 0.75:
            probs["Stagnation"] += c
        else:
            probs["Devolution"] += c
    for k in probs:
        probs[k] /= 2048

    outcome = max(probs, key=probs.get)

    st.success(f"**{outcome} ({probs[outcome]:.1%})**")
    st.markdown(f"**AC_sys = {AC_sys:.3f}**")

    # ===========================================================
    # VISUALIZATION
    # ===========================================================
    c1, c2 = st.columns(2)
    with c1:
        st.pyplot(plot_bloch_multivector(Statevector.from_instruction(qc.remove_final_measurements(inplace=False))))
    with c2:
        fig = go.Figure(data=[go.Bar(
            x=list(probs.keys()), 
            y=list(probs.values()),
            marker_color=["#00ff88", "#4488ff", "#ffaa00", "#ff4466"]
        )])
        fig.update_layout(yaxis_range=[0,1], title="Outcome Probabilities")
        st.plotly_chart(fig, use_container_width=True)

else:
    st.info("Set all sliders to 1.0 (except Conditioning = 0) → SEND → observe 100 % Transcendence.")
'''

with open("qcai_v1_9.py", "w") as f:
    f.write(code)

# ===============================================================
# STEP 3 — Run Streamlit app and open Cloudflare tunnel
# ===============================================================

!streamlit run qcai_v1_9.py --server.port=8501 --server.headless=true --server.address=0.0.0.0 > /dev/null 2>&1 &
print("\nStarting QCAI v1.9 app...")

!nohup ./cloudflared tunnel --url http://localhost:8501 --loglevel info > cloudflare.log 2>&1 &

# Wait for Cloudflare link
for i in range(60):
    time.sleep(1)
    try:
        log = open("cloudflare.log").read()
        url = re.search(r"https://[a-z0-9-]+\.trycloudflare\.com", log)
        if url:
            print("\n" + "="*80)
            print("      QCAI v1.9 — Quantum Consciousness Interface")
            print("="*80)
            print(f"      LIVE URL: {url.group(0)}")
            print("="*80)
            print("      Tip: All = 1 (except Conditioning = 0) → 100 % Transcendence")
            print("="*80)
            break
    except Exception:
        pass
else:
    print("Timeout — Re-run cell to obtain URL.")
