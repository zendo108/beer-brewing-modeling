import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import pandas as pd
import unittest

# Parameters for fermentation
K_fermentation = 0.1  # Fermentation rate constant (1/s)
Y_ethanol = 0.5       # Molar fraction of ethanol produced per sugar consumed
Y_CO2 = 0.5           # Molar fraction of CO2 produced per sugar consumed
C_sugar_0 = 100       # Initial sugar concentration (mol/L)
C_ethanol_0 = 0       # Initial ethanol concentration (mol/L)
C_CO2_0 = 0           # Initial CO2 concentration (mol/L)
m = 1.0               # Mass (kg)
c_p = 4184            # Specific heat capacity (J/kg*K)
Q_fermentation = 500  # Heat generated during fermentation (J/s)
Q_cooling = 500       # Cooling heat removal (J/s)
T_0 = 25              # Initial temperature (Celsius)
pH_0 = 5.0            # Initial pH
K_pH = 0.01           # Rate of pH decrease
buffer_capacity = 0.1  # Buffer capacity to regulate pH within a realistic range

def fermentation_odes(t, y):
    """
    Defines the ODEs for fermentation.
    y = [C_sugar, C_ethanol, C_CO2, T, pH]
    """
    C_sugar, C_ethanol, C_CO2, T, pH = y

    # ODEs
    dC_sugar_dt = -K_fermentation * C_sugar
    dC_ethanol_dt = Y_ethanol * K_fermentation * C_sugar
    dC_CO2_dt = Y_CO2 * K_fermentation * C_sugar
    dT_dt = (Q_fermentation - Q_cooling) / (m * c_p)
    
    # Apply buffer to regulate pH
    dpH_dt = max(-K_pH * C_sugar, -buffer_capacity) if pH > 4 else 0

    return [dC_sugar_dt, dC_ethanol_dt, dC_CO2_dt, dT_dt, dpH_dt]

# Initial conditions
y0 = [C_sugar_0, C_ethanol_0, C_CO2_0, T_0, pH_0]

# Time span for the simulation
t_span = (0, 300)  # 300 seconds
t_eval = np.linspace(*t_span, 500)  # 500 time points

# Solve the ODEs
solution = solve_ivp(fermentation_odes, t_span, y0, method='RK45', t_eval=t_eval)

# Extract results
time = solution.t
C_sugar = solution.y[0]
C_ethanol = solution.y[1]
C_CO2 = solution.y[2]
T = solution.y[3]
pH = solution.y[4]

# Save results to a CSV file
results = pd.DataFrame({
    "Time (s)": time,
    "Sugar (mol/L)": C_sugar,
    "Ethanol (mol/L)": C_ethanol,
    "CO2 (mol/L)": C_CO2,
    "Temperature (C)": T,
    "pH": pH
})
results.to_csv("fermentation_results.csv", index=False)

# Plot results
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(time, C_sugar, label="Sugar (mol/L)", color="blue")
plt.xlabel("Time (s)")
plt.ylabel("Concentration (mol/L)")
plt.title("Sugar Concentration")
plt.legend()
plt.grid()

plt.subplot(2, 2, 2)
plt.plot(time, C_ethanol, label="Ethanol (mol/L)", color="orange")
plt.xlabel("Time (s)")
plt.ylabel("Concentration (mol/L)")
plt.title("Ethanol Production")
plt.legend()
plt.grid()

plt.subplot(2, 2, 3)
plt.plot(time, C_CO2, label="CO2 (mol/L)", color="green")
plt.xlabel("Time (s)")
plt.ylabel("Concentration (mol/L)")
plt.title("CO2 Production")
plt.legend()
plt.grid()

plt.subplot(2, 2, 4)
plt.plot(time, T, label="Temperature (C)", color="red")
plt.plot(time, pH, label="pH", color="purple")
plt.xlabel("Time (s)")
plt.ylabel("Value")
plt.title("Temperature and pH")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

# Unit tests for fermentation module
class TestFermentationModule(unittest.TestCase):

    def test_sugar_depletion(self):
        """Test that sugar concentration decreases over time."""
        self.assertTrue(all(C_sugar[i] >= C_sugar[i+1] for i in range(len(C_sugar)-1)))

    def test_ethanol_production(self):
        """Test that ethanol concentration increases over time."""
        self.assertTrue(all(C_ethanol[i] <= C_ethanol[i+1] for i in range(len(C_ethanol)-1)))

    def test_CO2_production(self):
        """Test that CO2 concentration increases over time."""
        self.assertTrue(all(C_CO2[i] <= C_CO2[i+1] for i in range(len(C_CO2)-1)))

    def test_temperature_stability(self):
        """Test that temperature changes are within a reasonable range."""
        self.assertTrue(all(20 <= T[i] <= 30 for i in range(len(T))))

    def test_pH_regulation(self):
        """Test that pH stays within the natural range."""
        self.assertTrue(all(4.0 <= pH[i] <= 7.0 for i in range(len(pH))))

if __name__ == "__main__":
    unittest.main()
