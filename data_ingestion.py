import pandas as pd
import numpy as np
import json

# Simulate catalyst experimental data
np.random.seed(42)
n_samples = 1000
data = {
    "composition": [f"Ni{np.random.randint(50,80)}Fe{np.random.randint(10,30)}" for _ in range(n_samples)],
    "current_density": np.random.uniform(0.5, 2.5, n_samples),
    "overpotential": np.random.uniform(0.15, 0.35, n_samples),
    "temperature": np.random.uniform(60, 90, n_samples)
}
df = pd.DataFrame(data)
df.to_csv("raw_experiments.csv", index=False)

# Generate summary JSON
summary = {
    "samples": n_samples,
    "mean_current_density": float(df.current_density.mean()),
    "mean_overpotential": float(df.overpotential.mean())
}
with open("data_summary.json", "w") as f:
    json.dump(summary, f, indent=2)

print("Data ingestion complete.")
