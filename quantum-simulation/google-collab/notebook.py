
# === v4.2 QUANTUM CONSCIOUSNESS — 60s WAIT + 100% URL ===
!pkill -f streamlit
!pkill -f cloudflared
!sleep 3

!pip install streamlit qiskit qiskit-aer matplotlib plotly numpy -q
import os
if not os.path.exists("cloudflared"):
    !wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O cloudflared
    !chmod +x cloudflared

# === v4.2 CODE — FULLY FIXED ===
code = '''
import streamlit as st
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error
import plotly.graph_objects as go

st.set_page_config(page_title="v4.2 Quantum Consciousness", layout="wide")
st.title("CONSCIOUS NAVIGATION v4.2")
st.markdown("**Five Laws → Quantum Dynamics**")

# Law I
st.sidebar.markdown("### Law I — Dual Potential")
conditioning_strength = st.sidebar.slider("Conditioning", 0.0, 1.0, 0.3)
transcendence_tendency = 1.0 - conditioning_strength

# Law II
st.sidebar.markdown("### Law II — Equilibrium")
restraint = st.sidebar.slider("Restraint", 0.0, 1.0, 0.5)
expansion = st.sidebar.slider("Expansion", 0.0, 1.0, 0.5)
equilibrium = 1.0 - abs(restraint - expansion)

# Actors (Law III)
n = st.sidebar.slider("Actors", 1, 5, 3)
actors = []
balanced_present = False
for i in range(n):
    with st.sidebar:
        st.markdown(f"#### Actor {i+1}")
        typ = st.selectbox("Stance",
            ["Balanced", "Transcendent", "Restrained-Bal", "Chaos-Bal",
             "Rigid", "Conditioned", "Restrained-Ext", "Chaos-Ext"],
            key=f"t{i}")
        if typ in ["Balanced", "Transcendent"]: balanced_present = True
        A = st.slider("Awareness", 0.0, 1.0, 0.9 if "Bal" in typ or "Trans" in typ else 0.4, 0.05, key=f"a{i}")
        P = st.slider("Compassion", 0.0, 1.0, 0.9 if "Trans" in typ else 0.7 if "Bal" in typ else 0.3, 0.05, key=f"p{i}")
        S = st.slider("Somatic", 0.0, 1.0, 0.9 if "Trans" in typ else 0.7 if "Bal" in typ else 0.4, 0.05, key=f"s{i}")
        Cal = st.slider("Calibration", 0.0, 1.0, 0.95 if "Trans" in typ else 0.7 if "Bal" in typ else 0.3, 0.05, key=f"c{i}")
        actors.append({"A":A, "P":P, "S":S, "Cal":Cal, "type":typ})

# Law IV
witness_depth = st.sidebar.slider("Law IV — Witness Depth", 0.0, 1.0, 0.8)
witness_effect = witness_depth * np.prod([a["S"] for a in actors]) ** (1/n) if actors else 1.0

# Law V
AC_sys = np.prod([a["Cal"] * a["S"] for a in actors]) ** (1/len(actors)) if actors else 1.0
AC_sys *= (equilibrium + witness_effect) / 2
st.sidebar.metric("Law V — AC_sys", f"{AC_sys:.3f}")

noise_level = st.sidebar.slider("Noise", 0.0, 0.5, 0.0)
shots = st.sidebar.slider("Shots", 256, 4096, 2048)

# Circuit
qc = QuantumCircuit(n, n)
for i in range(n): qc.h(i)

for i, a in enumerate(actors):
    control = {"Balanced":0,"Transcendent":0,"Restrained-Bal":0.3,"Chaos-Bal":0.3,
               "Rigid":0.8,"Conditioned":0.6,"Restrained-Ext":1.0,"Chaos-Ext":1.0}.get(a["type"],0.7)
    control_eff = control * (1 - a["S"] * a["Cal"]) * conditioning_strength
    if control_eff > 0.5: qc.ry(control_eff * np.pi, i)
    qc.ry(a["A"] * a["P"] * np.pi / 3 * transcendence_tendency, i)
    qc.rz(a["Cal"] * np.pi * witness_effect, i)

for i in range(n-1): qc.cz(i, i+1)
for i in range(n): qc.ry(AC_sys * np.pi / (3 if balanced_present else 6), i)
for i in range(n): qc.h(i)
for i in range(n): qc.measure(i, i)

# Simulate
sim = AerSimulator()
t_qc = transpile(qc, sim)
if noise_level > 0:
    noise = NoiseModel()
    noise.add_all_qubit_quantum_error(depolarizing_error(noise_level, 1), ["ry", "rz", "h"])
    noise.add_all_qubit_quantum_error(depolarizing_error(noise_level * 2, 2), ["cz"])
    job = sim.run(t_qc, shots=shots, noise_model=noise)
else:
    job = sim.run(t_qc, shots=shots)
result = job.result()
counts = result.get_counts()

# Classify
def classify(bits):
    ratio = sum(int(b) for b in bits) / n
    if ratio < 0.2: return "Transcendence"
    elif ratio < 0.4: return "Evolution"
    elif ratio < 0.6: return "Stagnation"
    else: return "Devolution"

probs = {k:0 for k in ["Transcendence","Evolution","Stagnation","Devolution"]}
for bits, c in counts.items():
    probs[classify(bits)] += c / shots

# Display
c1, c2 = st.columns(2)
with c1:
    st.subheader("Bloch Field")
    sv = Statevector.from_instruction(qc.remove_final_measurements(inplace=False))
    st.pyplot(plot_bloch_multivector(sv))
with c2:
    st.subheader("Outcomes")
    st.pyplot(plot_histogram(counts))

fig = go.Figure(data=[go.Bar(x=list(probs.keys()), y=list(probs.values()),
                             marker_color=["#00ff88","#4488ff","#ffaa00","#ff4466"])])
fig.update_layout(yaxis_range=[0,1])
st.plotly_chart(fig, use_container_width=True)

D_f = np.log10(sum(a["A"]*a["P"]*a["Cal"]*a["S"] for a in actors) * AC_sys + 1e-10)
st.metric("Fractal Dimension", f"{D_f:.3f}")
st.success(f"**Transcendence: {probs['Transcendence']:.1%} | Balanced: {'Yes' if balanced_present else 'No'}**")

with st.expander("Five Laws Active"):
    st.markdown("""
- **Law I**: Dual Potential → Conditioning vs Transcendence
- **Law II**: Equilibrium → Restraint ↔ Expansion
- **Law III**: Relational Field → CZ + non-collapse if balanced
- **Law IV**: Witnessing → Phase alignment via Somatic
- **Law V**: Adaptive Coherence → Final rotation driver
    """)
'''

with open("app.py", "w") as f: f.write(code)

# === START STREAMLIT ===
!streamlit run app.py --server.port=8501 --server.headless=true --server.address=0.0.0.0 > /dev/null 2>&1 &

# === START CLOUDFLARE + WAIT 60 SECONDS ===
print("\nStarting Cloudflare Tunnel... (please wait up to 60 seconds)")
!nohup ./cloudflared tunnel --url http://localhost:8501 --loglevel info > cloudflare.log 2>&1 &
import time, re
url_found = False
for i in range(60):
    time.sleep(1)
    try:
        log = open("cloudflare.log", "r").read()
        url_match = re.search(r"https://[a-z0-9-]+\.trycloudflare\.com", log)
        if url_match:
            url = url_match.group(0)
            print("\n" + "="*80)
            print("     v4.2 QUANTUM CONSCIOUSNESS IS LIVE")
            print("="*80)
            print(f"     LIVE URL: {url}")
            print("="*80)
            print("     CLICK ABOVE → TEST: 1 Balanced Actor → Transcendence ↑")
            print("="*80)
            url_found = True
            break
    except:
        pass
if not url_found:
    print("Still waiting... trying one more time...")
    time.sleep(10)
    try:
        log = open("cloudflare.log", "r").read()
        url_match = re.search(r"https://[a-z0-9-]+\.trycloudflare\.com", log)
        if url_match:
            url = url_match.group(0)
            print("\n" + "="*80)
            print("     v4.2 QUANTUM CONSCIOUSNESS IS LIVE")
            print("="*80)
            print(f"     LIVE URL: {url}")
            print("="*80)
            print("     CLICK ABOVE")
            print("="*80)
        else:
            print("Final timeout. Run cell again.")
    except:
        print("Error reading log. Run cell again.")
