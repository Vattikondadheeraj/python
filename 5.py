import pandas as pd
class Employee:
    def  setemployee(self):
        self.name=input("enter the name")
        self.no=int(input("enter the number"))
    def getemployee(self):
        print(self.name,self.no)
    
    
df=pd.DataFrame()
s=Employee()
#print(Employee.__dict__)
print(df.__dict__)