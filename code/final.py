# NOTE: In the place of pd.read_excel(dummyok.xlsx) dont forget to change the name of the file.
# df = pd.read_excel('/path/to/dummyok.xlsx') change the path as above if you want to give the file path.

print("\nConditions for voltage_ph1,voltage_ph2,voltage_ph3")

import pandas as pd
print("\nvoltage_ph1\n")

# Read the Excel file

df = pd.read_excel('dummyok.xlsx')
load_ranges = {
    '0-20': {'above': 0, 'below': 0},
    '20-50': {'above': 0, 'below': 0},
    '50-100': {'above': 0, 'below': 0},
    '100+': {'above': 0, 'below': 0},
}

for index, row in df.iterrows():
    load_factor = row['load_factor']
    voltage_ph1 = row['voltage_ph1']
    for key in load_ranges:
        if '-' in key:
            low, high = key.split('-')
            if load_factor >= int(low) and load_factor <= int(high):
                if voltage_ph1 < 180:
                    load_ranges[key]['below'] += 1
                elif voltage_ph1 > 265:
                    load_ranges[key]['above'] += 1
        else:
            if load_factor > int(key[:-1]):
                if voltage_ph1 < 180:
                    load_ranges[key]['below'] += 1
                elif voltage_ph1 > 265:
                    load_ranges[key]['above'] += 1

total_values = df['voltage_ph1'].count()

for key in load_ranges:
    if total_values > 0:
        if '-' in key:
            low, high = key.split('-')
            range_str = f"{low}-{high}"
        else:
            range_str = key
        percentage_above_265 = (load_ranges[key]['above'] / total_values) * 100
        percentage_below_180 = (load_ranges[key]['below'] / total_values) * 100

        # Print the results
        print(f"The percentage of values in the voltage_ph1 for the load factor range {range_str} that are above 265 is {round(percentage_above_265,2)}%")
        print(f"The percentage of values in the voltage_ph1 for the load factor range {range_str} that are below 180 is {round(percentage_below_180,2)}%")
    else:
        print("No values in the Excel sheet meet the conditions") 



# For voltage_ph2

print("\nvoltage_ph2\n")

load_ranges = {
    '0-20': {'above': 0, 'below': 0},
    '20-50': {'above': 0, 'below': 0},
    '50-100': {'above': 0, 'below': 0},
    '100+': {'above': 0, 'below': 0},
}

for index, row in df.iterrows():
    load_factor = row['load_factor']
    voltage_ph2 = row['voltage_ph2']  # Change variable name to voltage_ph2
    for key in load_ranges:
        if '-' in key:
            low, high = key.split('-')
            if load_factor >= int(low) and load_factor <= int(high):
                if voltage_ph2 < 180:
                    load_ranges[key]['below'] += 1
                elif voltage_ph2 > 265:
                    load_ranges[key]['above'] += 1
        else:
            if load_factor > int(key[:-1]):
                if voltage_ph2 < 180:
                    load_ranges[key]['below'] += 1
                elif voltage_ph2 > 265:
                    load_ranges[key]['above'] += 1

total_values = df['voltage_ph2'].count()  # Change column name to voltage_ph2

for key in load_ranges:
    if total_values > 0:
        if '-' in key:
            low, high = key.split('-')
            range_str = f"{low}-{high}"
        else:
            range_str = key
        percentage_above_265 = (load_ranges[key]['above'] / total_values) * 100
        percentage_below_180 = (load_ranges[key]['below'] / total_values) * 100

        # Print the results
        print(f"The percentage of values in the voltage_ph2 for the load factor range {range_str} that are above 265 is {round(percentage_above_265,2)}%")
        print(f"The percentage of values in the voltage_ph2 for the load factor range {range_str} that are below 180 is {round(percentage_below_180,2)}%")
    else:
        print("No values in the Excel sheet meet the conditions")

# For voltage_ph3
import pandas as pd
print("\nvoltage_ph3\n")

load_ranges = {
    '0-20': {'above': 0, 'below': 0},
    '20-50': {'above': 0, 'below': 0},
    '50-100': {'above': 0, 'below': 0},
    '100+': {'above': 0, 'below': 0},
}

for index, row in df.iterrows():
    load_factor = row['load_factor']
    voltage_ph3 = row['voltage_ph3']
    for key in load_ranges:
        if '-' in key:
            low, high = key.split('-')
            if load_factor >= int(low) and load_factor <= int(high):
                if voltage_ph3 < 180:
                    load_ranges[key]['below'] += 1
                elif voltage_ph3 > 265:
                    load_ranges[key]['above'] += 1
        else:
            if load_factor > int(key[:-1]):
                if voltage_ph3 < 180:
                    load_ranges[key]['below'] += 1
                elif voltage_ph3 > 265:
                    load_ranges[key]['above'] += 1

total_values = df['voltage_ph3'].count()

for key in load_ranges:
    if total_values > 0:
        if '-' in key:
            low, high = key.split('-')
            range_str = f"{low}-{high}"
        else:
            range_str = key
        percentage_above_265 = (load_ranges[key]['above'] / total_values) * 100
        percentage_below_180 = (load_ranges[key]['below'] / total_values) * 100

        # Print the results
        print(f"The percentage of values in the voltage_ph3 for the load factor range {range_str} that are above 265 is {round(percentage_above_265,2)}%")
        print(f"The percentage of values in the voltage_ph3 for the load factor range {range_str} that are below 180 is {round(percentage_below_180,2)}%")
    else:
        print("No values in the Excel sheet meet the conditions")


# Conditions for temp_r,temp_y,temp_b
print("\nConditions for temp_r,temp_y,temp_b")

print("\nFor temp_r\n")

load_ranges = {
    '0-20': {'above': 0, 'below': 0},
    '20-50': {'above': 0, 'below': 0},
    '50-100': {'above': 0, 'below': 0},
    '100+': {'above': 0, 'below': 0},
}

for index, row in df.iterrows():
    load_factor = row['load_factor']
    temp_r = row['temp_r']
    for key in load_ranges:
        if '-' in key:
            low, high = key.split('-')
            if load_factor >= int(low) and load_factor <= int(high):
                if temp_r < 50:
                    load_ranges[key]['below'] += 1
                elif temp_r > 50:
                    load_ranges[key]['above'] += 1
        else:
            if load_factor > int(key[:-1]):
                if temp_r < 50:
                    load_ranges[key]['below'] += 1
                elif temp_r > 50:
                    load_ranges[key]['above'] += 1

total_values = df['temp_r'].count()

for key in load_ranges:
    if total_values > 0:
        if '-' in key:
            low, high = key.split('-')
            range_str = f"{low}-{high}"
        else:
            range_str = key
        percentage_above_50 = (load_ranges[key]['above'] / total_values) * 100
        percentage_below_50 = (load_ranges[key]['below'] / total_values) * 100

        # Print the results
        print(f"The percentage of values in the temp_r for the load factor range {range_str} that are above 50 is {round(percentage_above_50, 2)}%")
        print(f"The percentage of values in the temp_r for the load factor range {range_str} that are below 50 is {round(percentage_below_50, 2)}%")
    else:
        print("No values in the Excel sheet meet the conditions")

# For temp_y

print("\nFor temp_y\n")

load_ranges = {
    '0-20': {'above': 0, 'below': 0},
    '20-50': {'above': 0, 'below': 0},
    '50-100': {'above': 0, 'below': 0},
    '100+': {'above': 0, 'below': 0},
}

for index, row in df.iterrows():
    load_factor = row['load_factor']
    temp_y = row['temp_y']
    for key in load_ranges:
        if '-' in key:
            low, high = key.split('-')
            if load_factor >= int(low) and load_factor <= int(high):
                if temp_y < 50:
                    load_ranges[key]['below'] += 1
                elif temp_y > 50:
                    load_ranges[key]['above'] += 1
        else:
            if load_factor > int(key[:-1]):
                if temp_y < 50:
                    load_ranges[key]['below'] += 1
                elif temp_y > 50:
                    load_ranges[key]['above'] += 1

total_values = df['temp_y'].count()

for key in load_ranges:
    if total_values > 0:
        if '-' in key:
            low, high = key.split('-')
            range_str = f"{low}-{high}"
        else:
            range_str = key
        percentage_above_50 = (load_ranges[key]['above'] / total_values) * 100
        percentage_below_50 = (load_ranges[key]['below'] / total_values) * 100

        # Print the results
        print(f"The percentage of values in the temp_y for the load factor range {range_str} that are above 50 is {round(percentage_above_50, 2)}%")
        print(f"The percentage of values in the temp_y for the load factor range {range_str} that are below 50 is {round(percentage_below_50, 2)}%")
    else:
        print("No values in the Excel sheet meet the conditions")

# For temp_b

print("\nFor temp_b\n")

load_ranges = {
    '0-20': {'above': 0, 'below': 0},
    '20-50': {'above': 0, 'below': 0},
    '50-100': {'above': 0, 'below': 0},
    '100+': {'above': 0, 'below': 0},
}

for index, row in df.iterrows():
    load_factor = row['load_factor']
    temp_b = row['temp_b']
    for key in load_ranges:
        if '-' in key:
            low, high = key.split('-')
            if load_factor >= int(low) and load_factor <= int(high):
                if temp_b < 50:
                    load_ranges[key]['below'] += 1
                elif temp_b > 50:
                    load_ranges[key]['above'] += 1
        else:
            if load_factor > int(key[:-1]):
                if temp_b < 50:
                    load_ranges[key]['below'] += 1
                elif temp_b > 50:
                    load_ranges[key]['above'] += 1

total_values = df['temp_b'].count()

for key in load_ranges:
    if total_values > 0:
        if '-' in key:
            low, high = key.split('-')
            range_str = f"{low}-{high}"
        else:
            range_str = key
        percentage_above_50 = (load_ranges[key]['above'] / total_values) * 100
        percentage_below_50 = (load_ranges[key]['below'] / total_values) * 100

        # Print the results
        print(f"The percentage of values in the temp_b for the load factor range {range_str} that are above 50 is {round(percentage_above_50, 2)}%")
        print(f"The percentage of values in the temp_b for the load factor range {range_str} that are below 50 is {round(percentage_below_50, 2)}%")
    else:
        print("No values in the Excel sheet meet the conditions")
