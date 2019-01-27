import pandas as pd
import numpy as np

from sklearn import metrics
from sklearn.ensemble.forest import RandomForestRegressor
from matplotlib.pyplot import axis

# def add_datepart(df, colName):
#     col = df[colName]
#     targ_pre = re.sub('[]')
def setNumerics(df, colName):
    fld = df[colName]
    


pd.set_option('display.expand_frame_repr', False)

                        
df = pd.read_csv("ITM_20190121.csv")

# for i in df.columns:
#     print(i)
    
# print(df.isnull())
# print(df.isnull().any())

df = df.drop(columns="ID").drop(columns="Vin").drop(columns="ProcessedTimestamp")
df[[c for c in df if df[c].isnull().sum() < 2]]
# df = pd.DataFrame({"ReceivedTimestamp":pd.date_range('02:00:00', periods=4, freq='23H')})
ftr = [3600,60,1]
df = df[df["DeviceSerial"] != 108406724]
print(df.head(8))
for i in df["ReceivedTimestamp"]:
    newStr = i
    x = sum([a*b for a,b in zip(ftr, map(float,newStr.split(':')))])
    df["ReceivedTimestamp"] = x
    
print(df.head(10))
for i in df["TripState"]:
    print(i)
    if(i == "Engine On"):
        i = 1.0
    else:
        i = 0.0
    df.replace("Engine On", 1.0)
    
    i = float(i)
    print(i, "engine")

m = RandomForestRegressor(n_jobs=-1)

m.fit(df["TripState"], df["ReceivedTimestamp"])


print(df.head(30))
print("test run")
