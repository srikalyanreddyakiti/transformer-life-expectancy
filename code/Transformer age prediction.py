import pandas as pd
from sklearn.preprocessing import StandardScaler

# load data
data = pd.read_csv('age_data.csv')

# extract age column
age = data['age']

# apply standard scaling
scaler = StandardScaler()
age_scaled = scaler.fit_transform(age.to_numpy().reshape(-1, 1))

# create new dataframe with scaled age data
data_transformed = pd.concat([data.drop(['age'], axis=1), pd.DataFrame(age_scaled, columns=['age_scaled'])], axis=1)

# save transformed data to file
data_transformed.to_csv('age_data_transformed.csv', index=False)

