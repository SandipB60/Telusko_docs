class Students:
    insti = "KGP"

    def __init__(self, name, age, roll, sub1, sub2, sub3,cpu,ram):
        self.name = name
        self.age = age
        self.roll = roll
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.cpu=cpu
        self.ram=ram
        #self.lap = self.Laptop(self,self.cpu,self.ram)
        self.lap = self.Laptop(self.cpu, self.ram)
        if self.set_score() == True:
            self.result = "Pass"
        else:
            self.result = "Fail"

    def get_avg(self):
        return float((self.sub1 + self.sub2 + self.sub3) / 3)

    def get_total(self):
        return float((self.sub1 + self.sub2 + self.sub3))

    def set_score(self):
        if float(self.get_total()) >= 90.0 and float(self.get_avg()) >= 30.0:
            return True
        else:
            return  False

    def show(self):
        if self.sub1 >= 50:
            self.category="Science"
            self.schol="Scholership"
        else:
            self.category ="Arts"
            self.schol = "Non-Scholership"
        return self.category, self.schol
    def compare(self,other):
        if self.age >= other.age:
            return True
        else:
            return False

    @classmethod
    def institute(cls):
        return cls.insti

    @staticmethod
    def greet():
        return "Bye"

    class Laptop:
        comp ="Dell"
        def __init__(self,cpu,ram):
            self.cpu=cpu
            self.ram=ram
        def show(self):
            self.cond="Old"
            self.reissue="Re-issueable"
            return self.cpu,self.ram, str(self.cond),str(self.reissue)


s1=Students("Sandip",13,1,70,90,90,"i10","2gb")
s2=Students("Shah",20,2,40,30,10,"i20","4gb")
if s1.compare(s2)==True:
     print("S1 is older than S2")
else:
    print("S1 is younger than S2")


print(f"Name: {s1.name} Insti:{s1.institute()} Age:{s1.age} Roll No:{s1.roll} Total: {float(s1.get_total())} Avg: {float(s1.get_avg())} Result: {str(s1.result)}")
print(f"{s1.name} show {s1.show()}")
print(f"{s1.name} has laptop of Company: {s1.lap.comp} CPU:{s1.lap.cpu} RAM:{s1.lap.ram}")
print(f"{s1.name} has laptop of {s1.lap.show()}")
print(f'{s1.name} says {str(s1.greet())}')

print(f"Name: {s2.name} Insti:{s2.institute()} Age:{s2.age} Roll No:{s2.roll} Total: {float(s2.get_total())} Avg: {float(s2.get_avg())} Result: {str(s2.result)}")
print(f"{s2.name} show {s2.show()}")
print(f"{s2.name} has laptop of Company: {s2.lap.comp} CPU:{s2.lap.cpu} RAM:{s2.lap.ram}")
print(f"{s2.name} has laptop of {s2.lap.show()}")
print(f'{s2.name} says {str(s2.greet())}')