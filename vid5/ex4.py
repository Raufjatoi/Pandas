import pandas as pd
# Creating a DataFrame with integer data
df = pd.DataFrame({'Integers': [1, 2, 3, 4]})
# Converting integer to float
df['Floats'] = df['Integers'].astype(float)
print(df)
