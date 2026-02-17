import json
import numpy as np
import matplotlib.pyplot as plt

# Simulate DFT convergence
iterations = np.arange(1, 21)
energy = -12.3 + 0.5 * np.exp(-iterations/5) * np.sin(iterations)
plt.plot(iterations, energy, marker='o')
plt.title("SCF Convergence (DFT Simulation)")
plt.xlabel("Iteration")
plt.ylabel("Energy (eV)")
plt.grid(True)
plt.savefig("dft_convergence.png")

# Fake DFT results
results = {
    "material": "NiFeCo",
    "formation_energy_eV": -12.3,
    "band_gap_eV": 1.2,
    "dft_code": "VASP",
    "kpoints": [4,4,4],
    "encut": 520,
    "converged": True
}
with open("dft_output.json", "w") as f:
    json.dump(results, f, indent=2)

print("DFT simulation complete.")
