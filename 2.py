class A:
    a=222
    def method1(self):
        self.a=123
        self.b=345
    @classmethod
    def method2(cls):
        print(cls.a)
        
class B:
    def method3(self):
        self.a=999
        self.b=777
        s1=A()
        s1.method1()
        print(self.a,self.b,s1.a,s1.b)
        A.method2()
        
s2=B()
s2.method3()       