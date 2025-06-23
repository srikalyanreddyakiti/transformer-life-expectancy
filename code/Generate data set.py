import random

def generate_dataset(n_samples):
    dataset = []
    for i in range(n_samples):
        # Generate random load factor between 0.5 and 1.0
        load_factor = round(random.uniform(0.5, 1.0), 2)
        # Generate random oil temperature between 50°C and 90°C
        oil_temp = round(random.uniform(50, 90), 2)
        # Calculate ambient temperature based on oil temperature
        amb_temp = round(random.uniform(oil_temp - 10, oil_temp + 10), 2)
        # Calculate life expectancy using the calc_life_expectancy function
        life_expectancy = calc_life_expectancy(load_factor, oil_temp, amb_temp)
        # Add data to dataset
        dataset.append([load_factor, oil_temp, amb_temp, life_expectancy])
    return dataset

# Generate dataset with 1000 samples
dataset = generate_dataset(1000)
print(dataset[:10])  # Print first 10 samples
