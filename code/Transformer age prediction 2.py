import pandas as pd

# read in the parameter data from a CSV file
df = pd.read_csv('parameter_data.csv')

# convert the date column to a datetime object
df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')

# select the rows for the specified date
selected_date = pd.to_datetime('20-02-2023', format='%d-%m-%Y')
df_selected = df[df['date'] == selected_date]

# take the average of the values for each parameter
avg = df_selected.groupby(['parameter1', 'parameter2', 'parameter3']).mean()

print(avg)

