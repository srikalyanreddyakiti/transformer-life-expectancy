import numpy as np
import pandas as pd

# define parameters
num_samples = 1000
num_phases = 3
temp_mean = 70.0  # degrees Celsius
temp_std = 10.0   # degrees Celsius
current_mean = 100.0  # amps
current_std = 20.0     # amps
load_factor_mean = 0.8
load_factor_std = 0.1

# generate data
temps = np.random.normal(temp_mean, temp_std, size=(num_samples, num_phases))
currents = np.random.normal(current_mean, current_std, size=(num_samples, num_phases))
load_factors = np.random.normal(load_factor_mean, load_factor_std, size=num_samples)

# create dataframe
df = pd.DataFrame(data=np.hstack((temps, currents, load_factors.reshape(-1, 1))),
                  columns=[f"Temp Phase {i}" for i in range(num_phases)] +
                          [f"Current Phase {i}" for i in range(num_phases)] +
                          ["Load Factor"])

# save to Excel file
df.to_excel("transformer_data.xlsx", index=False)

# print sample data
print("Sample data:")
print(df.head())


