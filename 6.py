import pandas as pd

df=pd.read_csv("/home/dheeraj/Desktop/ml.csv")
df1=df.loc[:,'Units Sold':'Total Cost']
i=0
p0=p1=p2=p3=p4=p5=5
hx=p0+p1*df.iloc[i,8]+p2*df.iloc[i,9]+p3*df.iloc[i,10]+p4*df.iloc[i,11]+p5*df.iloc[i,12]
q=0.001
m=5000
sum=None
def sigma(j):
    global i
    sum=0
    if j==0:
        for i in range(1):
            sum=sum+hx-df.iloc[i,13]
    else:        
        for i in range(1):
           sum=sum+(hx-df.iloc[i,13])*df.iloc[i,7+j] 
    return sum

for k in range(100000):
    temp0=p0-q*(sigma(0))/1
    temp1=p1-q*(sigma(1))/1
    temp2=p2-q*(sigma(2))/1
    temp3=p2-q*(sigma(3))/1
    temp4=p2-q*(sigma(4))/1
    temp5=p2-q*(sigma(5))/1
    [p0,p1,p2,p3,p4,p5]=[temp0,temp1,temp2,temp3,temp4,temp5]
print(p0,p1,p2,p3,p4,p5)