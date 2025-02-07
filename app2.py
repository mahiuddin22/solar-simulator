import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Given Data
temperature = np.array([25, 26, 27, 28, 29, 30, 31])
dc_power = np.array([133.83, 132.9, 137.5, 138.7, 137.6, 136.7, 131.94])

# Create smooth interpolation
x_smooth = np.linspace(temperature.min(), temperature.max(), 300)
spline = make_interp_spline(temperature, dc_power, k=3)
y_smooth = spline(x_smooth)

# Plot
plt.figure(figsize=(8,5))
plt.plot(x_smooth, y_smooth, label="DC Power Curve", color='b')
plt.scatter(temperature, dc_power, color='r', label="Actual Data")
plt.axhline(y=np.mean(dc_power), color='g', linestyle='--', label="Avg Power (135.59 W)")

plt.xlabel("Temperature (°C)")
plt.ylabel("DC Power (W)")
plt.title("Simulation of DC Power vs Temperature")
plt.legend()
plt.grid(True)
plt.show()