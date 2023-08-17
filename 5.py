import pandas as pd
df=pd.read_csv("D:/Dataset/breast_cancer_analysis_DecisionTrees.csv")
print(df)
print(df.head(5))
print(df.tail(5))
print(df.info())
print(df.dtypes)
print(df.count())
print(df["symmetry_worst"]) 
