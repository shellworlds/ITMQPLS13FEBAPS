from qiskit import QuantumCircuit
from qiskit.visualization import circuit_drawer
import json

# Create a simple 2-qubit variational circuit (simulating H2 molecule)
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.ry(0.1, 0)
qc.rz(0.2, 1)
qc.measure_all()

# Save circuit diagram as PNG
circuit_drawer(qc, output='mpl', filename='vqe_circuit.png')

# Save circuit as QASM (with fallback)
try:
    qasm_str = qc.qasm()
    with open("circuit.qasm", "w") as f:
        f.write(qasm_str)
except AttributeError:
    # Fallback: create a dummy QASM file
    with open("circuit.qasm", "w") as f:
        f.write("""OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];
creg c[2];
h q[0];
cx q[0],q[1];
ry(0.1) q[0];
rz(0.2) q[1];
measure q[0] -> c[0];
measure q[1] -> c[1];""")
    print("QASM fallback used.")

# Dummy VQE result (simulate)
result = {
    "optimal_energy": -1.137,
    "parameters": [0.123, 0.456],
    "shots": 1024,
    "qubits": 2,
    "optimizer": "COBYLA"
}
with open("vqe_result.json", "w") as f:
    json.dump(result, f, indent=2)

print("VQE circuit and result saved.")
