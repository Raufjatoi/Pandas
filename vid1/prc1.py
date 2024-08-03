import pandas as pd # importing lib

## 1. Creating 
  
#lezz create a dataframe feel free to create your own
df = pd.DataFrame({"Rauf" : [20] , "Umar" : [19]} , index=['age'])
#print(df)

# now playb with series 
year_wise_age = pd.Series([13,14,15,16,17,18,19,20] , index=[2017,2018,2019,2020,2021,2022,2023,2024] , name="year wise my age series")
#print(year_wise_age)

## 2.Reading 

#lezz do some reading noe 
data = pd.read_csv("simple.csv")
#print(data.head()) # show five top rows default is 5
#play more with it like i show ya the tail the info details etc go on 

## 3.Writing

# lezz close up things with saving somethin lezz save both the series and the table we create

df.to_csv("save1.csv")
year_wise_age.to_csv("save2.csv")

#so this was all for this vid cya in 2nd vid 