import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Category': ['B', 'A', 'B', 'A'],
    'Value': [20, 10, 25, 15]
})

# Sort by 'Value'
sorted_df = df.sort_values('Value')

print(sorted_df)
