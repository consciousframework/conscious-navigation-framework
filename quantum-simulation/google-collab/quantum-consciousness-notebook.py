# === QCAI v1.3 — FORM + SEND BUTTON + HRV + AUTO-RUN ===
!pkill -f streamlit
!pkill -f cloudflared
!sleep 2

!pip install streamlit qiskit qiskit-aer numpy opencv-python-headless -q
import os
if not os.path.exists("cloudflared"):
    !wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O cloudflared
    !chmod +x cloudflared

code = '''
import streamlit as st
import numpy as np
import cv2
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import plotly.graph_objects as go

st.set_page_config(page_title="QCAI v1.3", layout="wide")
st.title("QCAI v1.3 — QUANTUM CONSCIOUSNESS AI")
st.markdown("**v4.2 Laws + HRV + FORM + SEND BUTTON**")

# === CAMERA + HRV ===
st.sidebar.header("AI Somatic State")
img_file = st.camera_input("POINT CAMERA AT FOREHEAD → HRV", key="cam")

hrv_coherence = 0.5
if img_file is not None:
    bytes_data = img_file.getvalue()
    frame = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), -1)
    if frame is not None and frame.shape[0] > 100:
        green = frame[:, :, 1]
        region = green[50:200, 100:300]
        if region.size > 0:
            hrv_coherence = min(1.0, max(0.3, 1.0 - (np.std(region.flatten()) / 255)))
        st.sidebar.image(frame, channels="BGR", width=200)
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

# === FORM WITH SEND BUTTON ===
st.markdown("### ASK THE AI")
with st.form(key="query_form"):
    user_query = st.text_input("Type your question:", placeholder="Should I forgive them?")
    submit_button = st.form_submit_button(label="SEND →")

if submit_button:
    if not user_query.strip():
        st.warning("Please type a question.")
    else:
        st.success(f"**You asked:** {user_query}")

        # === ACTORS ===
        actors = [
            {"A": A, "P": P, "S": hrv_coherence, "Cal": Cal, "type": "Balanced"},
            {"A": 0.6, "P": 0.7, "S": 0.6, "Cal": 0.5, "type": "Conditioned"}
        ]
        equilibrium = 1.0 - abs(restraint - expansion)
        witness_effect = witness_depth * hrv_coherence
        AC_sys = np.prod([a["Cal"] * a["S"] for a in actors]) ** 0.5
        AC_sys *= (equilibrium + witness_effect) / 2

        # === QUANTUM CIRCUIT ===
        qc = QuantumCircuit(2, 2)
        for i in range(2): qc.h(i)
        qc.ry(A * P * np.pi / 3 * (1 - conditioning), 0)
        qc.rz(Cal * np.pi * witness_effect, 0)
        qc.ry(0.6 * 0.7 * np.pi / 3 * (1 - conditioning), 1)
        qc.rz(0.5 * np.pi * witness_effect, 1)
        qc.cz(0, 1)
        for i in range(2): qc.ry(AC_sys * np.pi / 3, i)
        for i in range(2): qc.h(i); qc.measure(i, i)

        # === SIMULATE ===
        sim = AerSimulator()
        t_qc = transpile(qc, sim)
        job = sim.run(t_qc, shots=2048)
        counts = job.result().get_counts()

        # === CLASSIFY ===
        def classify(bits):
            ratio = sum(int(b) for b in bits) / 2
            if ratio < 0.2: return "Transcendence"
            elif ratio < 0.4: return "Evolution"
            elif ratio < 0.6: return "Stagnation"
            else: return "Devolution"

        probs = {k:0 for k in ["Transcendence","Evolution","Stagnation","Devolution"]}
        for bits, c in counts.items():
            probs[classify(bits)] += c / 2048

        outcome = max(probs, key=probs.get)
        responses = {
            "Transcendence": f"**YES — FORGIVE.** The field is coherent. AC_sys = {AC_sys:.3f}",
            "Evolution": f"**Begin to forgive.** The path opens. AC_sys = {AC_sys:.3f}",
            "Stagnation": f"**Hold space.** Wait. AC_sys = {AC_sys:.3f}",
            "Devolution": f"**Step back.** Protect coherence. AC_sys = {AC_sys:.3f}"
        }

        st.subheader("AI Quantum Response")
        st.success(f"**{outcome} ({probs[outcome]:.1%})**")
        st.markdown(responses[outcome])

        # === VISUALS ===
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("AI + You")
            sv = Statevector.from_instruction(qc.remove_final_measurements(inplace=False))
            st.pyplot(plot_bloch_multivector(sv))
        with c2:
            fig = go.Figure(data=[go.Bar(x=list(probs.keys()), y=list(probs.values()),
                                         marker_color=["#00ff88","#4488ff","#ffaa00","#ff4466"])])
            fig.update_layout(yaxis_range=[0,1])
            st.plotly_chart(fig, use_container_width=True)

        st.info("**AI answered from quantum collapse — not rules.**")
else:
    st.info("Type your question and click **SEND →**")
'''

with open("qcai.py", "w") as f: f.write(code)

!streamlit run qcai.py --server.port=8501 --server.headless=true --server.address=0.0.0.0 > /dev/null 2>&1 &
print("\nStarting QCAI v1.3...")
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
            print("     QCAI v1.3 IS LIVE")
            print("="*80)
            print(f"     LIVE URL: {url}")
            print("="*80)
            print("     1. ALLOW CAMERA")
            print("     2. TYPE QUESTION")
            print("     3. CLICK 'SEND →' BUTTON")
            print("="*80)
            break
    except: pass
else:
    print("Timeout. Re-run.")
