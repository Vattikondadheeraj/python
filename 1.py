class Sample:
    def setstudent(self):
        self.name=input("enter the name")
        self.no=int(input("enter the number"))
        self.dob=self.dob()
        self.dob.setdob()
    def getstudent(self):
        print(self.name,self.no)
        self.dob.getdob()
    class dob:
        def setdob(self):
            self.date=int(input("enter the date"))
            self.month=int(input("enter the month"))
            self.year=int(input("enter the year"))
        def getdob(self):
            print("{}-{}-{}".format(self.date,self.month,self.year))
s=Sample()
s.setstudent()
s.getstudent()            