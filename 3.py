class A:
    def method1(self):
        self.name=input("enter the name")
        self.no=input("enter the marks")
        print("A class")
class B(A):
    def method2(self):
        self.method1()
        print(self.name,self.no)
    
s=B()
s.method2()        
