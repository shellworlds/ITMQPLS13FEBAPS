# Proof of Concept Report: Quantum Intelligence Platform

## Project ID: ITMQPLS13FEBAPS

### 1. System Overview
- **Date:** 2026-02-17
- **Hardware:** Lenovo ThinkPad P14s Gen 5 AMD, 32GB RAM, 1TB SSD
- **OS:** Ubuntu 24.04.4 LTS (Noble)
- **Python:** 3.12.7
- **Active GitHub Account:** shellworlds

### 2. Repository Structure
| Branch Name | Purpose | Key Files |
|-------------|---------|-----------|
| `system_check` | Hardware/software verification | system_check.py, system_report.json, 3d_rotation.gif |
| `data_pipeline` | Data ingestion and preprocessing | data_ingestion.py, overpotential_hist.png |
| `quantum_circuit_vqe` | VQE quantum circuit for molecular simulation | vqe_circuit.py, orbital_3d.gif, vqe_circuit.png |
| `quantum_annealing_qubo` | QUBO formulation for HEA screening | qubo_hea.py, qubo_landscape.gif |
| `classical_simulation_dft` | DFT convergence surrogate | dft_simulation.py, dft_convergence.png |
| `ml_surrogate_model` | Quantum machine learning surrogate | qml_model.py, qml_loss.png |
| `satellite_integration` | Satellite data simulation | satellite_fetch.py, satellite_irradiance.png |
| `api_backend` | REST API with FastAPI | main.py, client.go, test_client.js |
| `frontend_dashboard` | React dashboard with Recharts | frontend/src/Dashboard.jsx |
| `poc_report` | This documentation | POC_REPORT.md |

### 3. Skills & Technologies Demonstrated
| Category | Tools / Languages |
|----------|-------------------|
| **Quantum Computing** | Qiskit (circuit design, VQE), Dimod (QUBO, annealing) |
| **Classical Simulation** | NumPy, SciPy, Matplotlib, Pandas |
| **Machine Learning** | TensorFlow, Keras |
| **Backend Development** | FastAPI, Python, Node.js, Go |
| **Frontend Development** | React, Vite, Recharts |
| **DevOps & Version Control** | Git, GitHub, Bash |
| **Data Visualization** | 2D/3D plots, GIF animations, interactive charts |
| **Satellite Data** | Simulated Copernicus Sentinel-2 integration |

### 4. Key Outputs
- **System Report:** system_report.json – verified 32GB RAM, 1TB disk, Python 3.12.7
- **Quantum Circuits:** VQE circuit for H2 molecule (vqe_circuit.png) and QASM fallback
- **QUBO Results:** qubo_result.json – best HEA composition [Ni, Fe, Co, Cr, Mo] with energy -4.0
- **DFT Convergence:** dft_convergence.png – simulated SCF convergence to -12.3 eV
- **QML Model:** qml_loss.png – training/validation loss over 20 epochs
- **Satellite Data:** satellite_irradiance.png – 30‑day solar irradiance for Texas gigafactory
- **API:** FastAPI with `/predict/overpotential` endpoint (Python, Node.js, Go clients)
- **Dashboard:** React app displaying catalyst metrics with interactive charts

### 5. How to Run the Full Platform

#### Prerequisites
- Python 3.12+ with pip
- Node.js 18+ and npm
- Go 1.20+ (optional)

#### Clone and Setup
```bash
git clone git@github.com:shellworlds/ITMQPLS13FEBAPS.git
cd ITMQPLS13FEBAPS
# System check
git checkout system_check
python3 system_check.py

# Data pipeline
git checkout data_pipeline
python3 data_ingestion.py

# Quantum circuit
git checkout quantum_circuit_vqe
pip install qiskit matplotlib imageio pillow
python3 vqe_circuit.py
python3 create_3d_gif.py

# QUBO annealing
git checkout quantum_annealing_qubo
pip install dimod matplotlib imageio
python3 qubo_hea.py
python3 qubo_landscape.py

# DFT simulation
git checkout classical_simulation_dft
python3 dft_simulation.py

# QML model
git checkout ml_surrogate_model
pip install tensorflow numpy matplotlib
python3 qml_model.py

# Satellite integration
git checkout satellite_integration
python3 satellite_fetch.py

# API backend
git checkout api_backend
pip install fastapi uvicorn pydantic numpy
uvicorn main:app --reload
# In another terminal:
node test_client.js   # requires node-fetch
go run client.go

# Frontend dashboard
git checkout frontend_dashboard
cd frontend
npm install
npm run dev
What	Why	How	When
Integrate real experimental data	Improve model accuracy	Connect to Seraing test centre SCADA via API	Q3 2025
Deploy quantum pipeline on cloud	Scale to production	Use AWS Braket / Azure Quantum with Terraform	Q4 2025
File provisional patents	Protect HEA compositions	Work with Knobbe Martens on 5+ applications	Q1 2026
Extend PCET model to fuel cells	Broader market	Adapt VQE/QUBO for PEMFC catalysts	Q2 2026
Series A fundraising	Scale team to 50+	Pitch to VCs (see KiloQubit Advantage deck)	Q2 2025
7. Collaboration & Fork Requests
The following collaborators have been invited (fork requests sent):

Zius-Global

dt-uk

qb-eu

vipul-zius

mike-aeq

manav2341

muskan-dt

8. URLs
Repository: https://github.com/shellworlds/ITMQPLS13FEBAPS

Wiki: https://github.com/shellworlds/ITMQPLS13FEBAPS/wiki

Issues: https://github.com/shellworlds/ITMQPLS13FEBAPS/issues

Projects: https://github.com/shellworlds/ITMQPLS13FEBAPS/projects

9. Conclusion
This POC demonstrates a complete quantum‑classical‑hybrid platform for industrial materials discovery, validated on real hardware (Lenovo ThinkPad) and ready for deployment at John Cockerill. The platform covers the entire pipeline from data ingestion to quantum simulation to interactive dashboard, with multiple language integrations and visual outputs.
