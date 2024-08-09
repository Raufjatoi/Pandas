import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'Numbers': [1, 2, 3, 4, 5]
})

# Define a mapping function
def square(x):
    return x * x

# Apply the function to the 'Numbers' column
df['Squared'] = df['Numbers'].map(square)

print(df)
