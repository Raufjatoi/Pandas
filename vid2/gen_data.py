
import pandas as pd
import numpy as np

# generate roll numbers
roll_numbers = np.arange(1, 67)

# generate IDs
ids = [f'STU{str(i).zfill(3)}' for i in roll_numbers]

# generate random marks between 50 and 100
marks = np.random.randint(50, 101, size=len(roll_numbers))

# creatin a DataFrame
df_students = pd.DataFrame({
    'Roll Number': roll_numbers,
    'ID': ids,
    'Marks': marks
})
df_students.to_csv("student.csv")
print(df_students)
