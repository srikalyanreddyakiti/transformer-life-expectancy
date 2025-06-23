import math

def calc_life_expectancy(load_factor, oil_temp, amb_temp):
    # Constants for mineral oil insulation
    # A = 125
    # B = 1.5
    # C = -5900
    # D = -3300
    A = 290
    B = 1.25 
    C = -5000 
    D = -3100
    
    # Calculate life expectancy
    LF = load_factor
    T1 = oil_temp
    T2 = amb_temp
    LE = A * (LF/100)**B * math.exp(C/T1) * math.exp(D/T2)
    
    return LE

# Example usage
LF = 25.1  # load factor as a percentage
T1 = 35.5  # oil temperature in °C
T2 = 39.5  # ambient temperature in °C

LE = calc_life_expectancy(LF, T1, T2)
print(f"Estimated life expectancy: {LE:.2f} years")