class A:
    def method1(self):
        self.a=111
        self.b=222
class B:
    def method(self):
        self.c=333
        self.d=444
class C(A,B):
    def method2(self):
        self.method()
        self.method1()
        print(self.a,self.b,self.c,self.d)
s=C()
s.method2()            