class anvit:
    def display(self):
      print("hi anvit")
a=anvit()
a.display()

class student:
    def __init__(self):
        self.name="anvit"
        self.rollno=15
        self.mark=90
    def talk(self):
        print("my name is:",self.name)
        print("my rollno is:",self.rollno)
        print("my mark is:",self.mark)
c=student()
c.talk()

# class student:
#     def __int__(self,name,mark):
#         self.name=name
#         self.mark=mark
#     def talk(self):
#         print("my name is:",self.name)
#         print("my marks are:",self.mark)
#
# c=student("anvit",90)
# c.talk()

#
# class student:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def talk(self):
#         print("my name is:",self.x)
#         print("my name is y:",self.y)
# s=student("a","b")
# s.talk()
#
# s.talk()

# class emp:
#     def __int__(self):
#         self.no=100
#         self.name="anvit"
# e=emp()
# print(e.__dict__)

# class emp:
#     def talk(self):
#         self.c=30
#         self.d=40
# e=emp()
# e.talk()
# print(e.__dict__)
#
# class emp:
#     def __int__(self):
#         self.a=10
#     def talk(self):
#         self.b=20
# e=emp()

# e.talk()
# e.c=40
# print(e.__dict__)


