mport pandas as pd
data = pd.read_csv("C:/Users/SPTIT-22/Desktop/data set/irisv.csv")
print(data)
print(data.head (5))
print(data.tail(10))
print(data["SepalWidthCm"])
print(data.info())
print(data.dtypes)
print(data.count())
