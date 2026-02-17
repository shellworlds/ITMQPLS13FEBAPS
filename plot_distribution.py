import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("raw_experiments.csv")
plt.hist(df.overpotential, bins=30, alpha=0.7, color='blue')
plt.title("Overpotential Distribution")
plt.xlabel("Overpotential (V)")
plt.ylabel("Frequency")
plt.savefig("overpotential_hist.png")
print("Histogram saved.")
