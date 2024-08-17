import pandas as pd

# Create two DataFrames
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

# Stack the DataFrames vertically
combined_df = pd.concat([df1, df2])

print(combined_df)
