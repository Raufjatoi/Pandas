# so i created some data see the gen_data.py to see how i do it lezz do some operations now
# first import pandas always
import pandas as pd # pd is just alias use p if ya like or anythin 

## 1. indexing and more 

#lezz peak around the data but first read it
data = pd.read_csv('student.csv')
#print(data.head())

# lezz do some operation we learn from the vid
#lezz add Marks to the m var 
m = data.Marks
#print(m)

# so this was easy less do some more 
# lez select just a specific val noe 
first_m = m[0] # or data.Marks[0] works too
#print(first_m)

# so basically this was a col we select noe lezz do for row lezz use loc and iloc 
first_row = data.iloc[0]
#print(first_row)

first_10_rows = data.iloc[:10] # : means everythin till 9 , 10 is exclusive
#print(first_10_rows)
# we can select just one val from each row too
first_10_rows_with_one_val_each = data.ID.iloc[:10]
#print(first_10_rows_with_one_val_each)

# noe lezz use some loc hehe 
first_five = data.loc[[0,1,2,3,4]]
#print(first_five) 

## 2. modying with loc 

col = ["Roll Number","ID","Marks"]
ind = [1,2,3,4,5]
df = data.loc[ind,col]
#print(df)

## 3. Assigning
mod_data = data["STU001"] = 'null'
print(mod_data)
