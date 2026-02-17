import dimod
import json

# Define QUBO for HEA screening (simplified example: 5 elements)
# Linear terms (bias for each element)
linear = {'Ni': -1.2, 'Fe': -0.8, 'Co': -1.0, 'Mo': -0.5, 'Cr': -0.7}
# Quadratic terms (interactions)
quadratic = {('Ni','Fe'): 0.3, ('Ni','Co'): 0.2, ('Fe','Mo'): -0.4, ('Co','Cr'): 0.1}
bqm = dimod.BinaryQuadraticModel(linear, quadratic, 0.0, dimod.BINARY)

# Solve with exact solver (small problem)
sampleset = dimod.ExactSolver().sample(bqm)
best = sampleset.first.sample
best_composition = [k for k,v in best.items() if v == 1]

result = {
    "best_composition": best_composition,
    "energy": sampleset.first.energy,
    "num_variables": len(bqm),
    "num_samples": len(sampleset)
}
with open("qubo_result.json", "w") as f:
    json.dump(result, f, indent=2)

print("QUBO result:", result)
