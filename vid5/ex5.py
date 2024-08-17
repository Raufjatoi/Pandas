import pandas as pd
# Creating a DataFrame with float data
df = pd.DataFrame({'Floats': [1.1, 2.2, 3.3, 4.4]})
# Converting float to integer (truncates decimal part)
df['Integers'] = df['Floats'].astype(int)
print(df)
