
class Student():
      insti='Telusko'

      def __init__(self,name,age,grade,m1,m2,m3,result):
          self.name = name
          self.age = age
          self.grade = grade
          self.m1=m1
          self.m2=m2
          self.m3=m3
          self.result=result
          self.lap=self.Laptop()

      def avg(self):
          return float((self.m1+self.m2+self.m3)/3)

      def compare(self,other):
          if self.grade != other.grade:
              #return True
              return "Not same grade"
          else:
              #False
              return "Same grade"

      def get_total(self):
          return (self.m1+self.m2+self.m3)

      def set_result(self):
          if float(self.avg()) >= 42.0:
              self.result="Pass"
          else:
              self.result = "Fail"

      @classmethod
      def intitute(cls):
          return Student.insti
      @staticmethod
      def general_info():
          return "Good bye"

      def show(self):
          #print(f"Student details: {self.name} -{self.age}")
          return (f"Stud Show-Student details: {self.name} -{self.age} :: {self.lap.show()}")

      class Laptop:
          def __init__(self):
              self.cpu="cpu 1"
              self.ram="ram 1"
          def show(self):
              return self.cpu,self.ram



s1=Student("Sandip",12,"8th",10,14,100,0)
s2=Student("Amrn",90,"5th",300,190,160,0)
s1.set_result()
s2.set_result()
lap1=Student.Laptop()

#print(f"Name :{s1.name} of {s1.age} age in {s1.grade} got avg:{s1.avg()} and total:{s1.get_total()} result: {s1.result} is {s1.compare(s2)})
print(f"Name :{s1.name} of {s1.age} age in {s1.grade} got avg:{s1.avg()} and total:{s1.get_total()} result: {s1.result} is {s1.compare(s2)}")
print(f"Name :{s2.name} of {s2.age} age in {s2.grade} got avg:{s2.avg()} and total:{s2.get_total()} result: {s2.result} is {s2.compare(s2)}")
print(f'Name of Institute is: {Student.intitute()} and {Student.general_info()}')
print(f"Student s1: {s1.show()}")
print(f"Student laptop: {s1.lap.show()} Student laptop:{lap1.show()}")



