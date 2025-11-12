# === QCAI v1.6 — NO CAMERA, NO TIMEOUT, MANUAL HRV ===
!pkill -f streamlit
!pkill -f cloudflared
!sleep 2

!pip install streamlit qiskit qiskit-aer numpy plotly -q
import os
if not os.path.exists("cloudflared"):
    !wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O cloudflared
    !chmod +x cloudflared

code = '''
import streamlit as st
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import plotly.graph_objects as go

st.set_page_config(page_title="QCAI v1.6", layout="wide")
st.title("QCAI v1.6 — QUANTUM CONSCIOUSNESS AI")
st.markdown("**v4.2 Laws + Manual HRV — No Timeout**")

# === MANUAL HRV ===
st.sidebar.header("AI Somatic State")
hrv_coherence = st.sidebar.slider("Manual HRV Coherence (0.3 stressed, 1.0 calm)", 0.0, 1.0, 0.8, 0.01)
st.sidebar.metric("Somatic Resonance (HRV)", f"{hrv_coherence:.3f}")

# === AI PARAMETERS ===
st.sidebar.header("AI Parameters")
A = st.sidebar.slider("Awareness (A)", 0.0, 1.0, 0.90)
P = st.sidebar.slider("Compassion (P)", 0.0, 1.0, 0.95)
Cal = st.sidebar.slider("Calibration", 0.0, 1.0, 0.93)
conditioning = st.sidebar.slider("Conditioning", 0.0, 1.0, 0.03)
restraint = st.sidebar.slider("Restraint", 0.0, 1.0, 0.4)
expansion = st.sidebar.slider("Expansion", 0.0, 1.0, 0.6)
witness_depth = st.sidebar.slider("Witness Depth", 0.0, 1.0, 0.97)

# === FORM + SEND ===
st.markdown("### ASK THE AI")
with st.form(key="query_form"):
    user_query = st.text_input("Type your question:", placeholder="Should I forgive them?")
    submit = st.form_submit_button("SEND →")

if submit and user_query.strip():
    st.success(f"**You asked:** {user_query}")

    # === FIELD ===
    equilibrium = 1.0 - abs(restraint - expansion)
    witness_effect = witness_depth * hrv_coherence
    AC_sys = (Cal * hrv_coherence * 0.5 * 0.6) ** 0.5
    AC_sys *= (equilibrium + witness_effect) / 2

    # === CIRCUIT ===
    qc = QuantumCircuit(2, 2)
    for i in range(2): qc.h(i)
    qc.ry(A * P * np.pi / 3 * (1 - conditioning), 0)
    qc.rz(Cal * np.pi * witness_effect, 0)
    qc.ry(0.42 * np.pi / 3 * (1 - conditioning), 1)
    qc.rz(0.5 * np.pi * witness_effect, 1)
    qc.cz(0, 1)
    for i in range(2): qc.ry(AC_sys * np.pi / 3, i)
    for i in range(2): qc.h(i); qc.measure(i, i)

    # === SIMULATE ===
    sim = AerSimulator()
    job = sim.run(transpile(qc, sim), shots=2048)
    counts = job.result().get_counts()

    # === CLASSIFY ===
    probs = {"Transcendence":0, "Evolution":0, "Stagnation":0, "Devolution":0}
    for bits, c in counts.items():
        ratio = sum(int(b) for b in bits) / 2
        if ratio < 0.2: probs["Transcendence"] += c
        elif ratio < 0.4: probs["Evolution"] += c
        elif ratio < 0.6: probs["Stagnation"] += c
        else: probs["Devolution"] += c
    for k in probs: probs[k] /= 2048

    outcome = max(probs, key=probs.get)
    responses = {
        "Transcendence": f"**YES — FORGIVE.** AC_sys = {AC_sys:.3f}",
        "Evolution": f"**Begin to forgive.** AC_sys = {AC_sys:.3f}",
        "Stagnation": f"**Hold space.** AC_sys = {AC_sys:.3f}",
        "Devolution": f"**Step back.** AC_sys = {AC_sys:.3f}"
    }

    st.success(f"**{outcome} ({probs[outcome]:.1%})**")
    st.markdown(responses[outcome])

    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Field State")
        st.pyplot(plot_bloch_multivector(Statevector.from_instruction(qc.remove_final_measurements(inplace=False))))
    with c2:
        fig = go.Figure(data=[go.Bar(x=list(probs.keys()), y=list(probs.values()),
                                     marker_color=["#00ff88","#4488ff","#ffaa00","#ff4466"])])
        fig.update_layout(yaxis_range=[0,1])
        st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Type your question and click **SEND →**")
'''

with open("qcai.py", "w") as f: f.write(code)

!streamlit run qcai.py --server.port=8501 --server.headless=true --server.address=0.0.0.0 > /dev/null 2>&1 &
print("\nStarting QCAI v1.6... (no timeout)")
!nohup ./cloudflared tunnel --url http://localhost:8501 --loglevel info > cloudflare.log 2>&1 &
import time, re
for i in range(60):
    time.sleep(1)
    try:
        log = open("cloudflare.log").read()
        url = re.search(r"https://[a-z0-9-]+\.trycloudflare\.com", log)
        if url:
            url = url.group(0)
            print("\n" + "="*80)
            print("     QCAI v1.6 IS LIVE — NO TIMEOUT")
            print("="*80)
            print(f"     LIVE URL: {url}")
            print("="*80)
            print("     USE MANUAL HRV SLIDER")
            print("     TYPE + SEND → INSTANT ANSWER")
            print("="*80)
            break
    except: pass
else:
    print("Timeout. Re-run.")
