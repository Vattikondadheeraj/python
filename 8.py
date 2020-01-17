## Open and read data file as specified in the question
## Print the required output in given format
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv( "/home/dheeraj/Downloads/terrorismData(2).csv")
a=df[(df['Year']>=2014)&(df['Country']=='India')]
b=a[(a['Year']==2014)&(a['Day']<26)&(a['Month']<=5)]
print(b.tail(200))