import json
import numpy as np
import matplotlib.pyplot as plt

# Simulate satellite data for a location (Baytown, Texas)
dates = np.arange('2025-01-01', '2025-02-01', dtype='datetime64[D]')
irradiance = np.random.uniform(200, 800, len(dates))
plt.figure(figsize=(10,5))
plt.plot(dates, irradiance, marker='o', linestyle='-')
plt.title("Solar Irradiance from Sentinel-2 (Simulated)")
plt.xlabel("Date")
plt.ylabel("W/m²")
plt.grid(True)
plt.savefig("satellite_irradiance.png")

data = {
    "location": "Baytown, Texas (John Cockerill Gigafactory)",
    "period": "2025-01",
    "mean_irradiance": float(np.mean(irradiance)),
    "max_irradiance": float(np.max(irradiance)),
    "min_irradiance": float(np.min(irradiance)),
    "source": "Copernicus Sentinel-2 (simulated)"
}
with open("satellite_data.json", "w") as f:
    json.dump(data, f, indent=2)

print("Satellite data simulation complete.")
