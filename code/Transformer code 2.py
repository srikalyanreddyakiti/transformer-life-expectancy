import numpy as np
import pandas as pd

# define parameters
num_samples = 1000
num_phases = 3
temp_min = 0.0   # degrees Celsius
temp_max = 120.0 # degrees Celsius
current_min = 0.0   # amps
current_max = 33.3  # amps
load_factor_mean = 0.8
load_factor_std = 0.1
A = 1e14     # pre-exponential factor
Ea = 1e5    # activation energy (J/mol)
k = 8.62e-5  # Boltzmann constant (eV/K)
expected_life = 40  # years

# generate data
temps = np.random.uniform(temp_min, temp_max, size=(num_samples, num_phases))
currents = np.random.uniform(current_min, current_max, size=(num_samples, num_phases))
load_factors = np.random.normal(load_factor_mean, load_factor_std, size=num_samples)

# calculate aging rate
T = temps.mean(axis=1) + 273.15
R = A * np.exp(-Ea/(k*T))

# calculate age
age = expected_life - (1 / (R * expected_life))

# replace negative and infinite values with NaN
age[age < 0] = np.nan
age[~np.isfinite(age)] = np.nan

# replace NaN values with expected life
age[np.isnan(age)] = expected_life

# convert age to pandas Series
age_series = pd.Series(age, name="Age", dtype=np.float64)

# create dataframe
df = pd.DataFrame(data=np.hstack((temps, currents, load_factors.reshape(-1, 1))),
                  columns=[f"Temp Phase {i}" for i in range(num_phases)] +
                          [f"Current Phase {i}" for i in range(num_phases)] +
                          ["Load Factor"])
df = pd.concat([df, age_series], axis=1)

# save to Excel file
df.to_excel("transformer_data_2.xlsx", index=False)

# print sample data
print("Sample data:")
print(df.head())
