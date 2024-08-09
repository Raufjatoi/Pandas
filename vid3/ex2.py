import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'Names': ['Alice', 'Bob', 'Charlie', 'David']
})

# Define a custom function
def greet(name):
    return f"Hello, {name}!"

# Apply the function to the 'Names' column
df['Greeting'] = df['Names'].apply(greet)

print(df)
