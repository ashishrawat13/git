#ques_1.
class circle:
    print("***blueprint for circle\n")
    print("enter the radius:")
    def __init__(self,radius):
        self.radius=radius
    def getarea(self):
        return 3.14*self.radius**2
    def getc(self):
       return 2*3.14*self.radius
r=int(input())
obj=circle(r)
print('area of circle:',obj.getarea())
print('circumference of circle:',obj.getc())
#ques_2.
class Student:
    def __init__(self,name,Rno):
        self.Name=name
        self.rno=Rno
    def setAge(self,age):
        self.Age=age
    def setMarks(self,marks):
        self.mark=marks
    def Display(self):
        print("Name: {}".format(self.Name))
        print("Roll No: {}".format(self.rno))
        print("Age: {}".format(self.Age))
        print("Marks: {}".format(self.mark))
name=input("Please Enter The Name of the Student ")
rollno=int(input("Please Enter The RollNo of the Student "))
age=int(input("Please Enter The Age of the Student "))
marks=int(input("Please Enter The Marks of the Student "))

S1=Student(name,rollno)
S1.setAge(age)
S1.setMarks(marks)
S1.Display()
#ques_3.
class Temp:
    def convertFahrenheit(self, Cel):
        self.Celc = Cel
        self.Farh = ((self.Celc * 9) / 5) + 32
        print("The Farh Conversion of {} is {}".format(self.Celc, self.Farh))

    def convertCelcius(self, Farh):
        self.Farh = Farh
        self.Cel = (self.Farh - 32) * 5 / 9
        print("The Celcius Conversion of {} is {}".format(self.Farh, self.Cel))


choice = ['1', '2']
T = Temp()
a = input("Input 1 for Converion to F and 2 for Conversion to C")
if a in choice:
    if a == '1':
        cel = int(input("Enter Temprature in Celcius"))
        T.convertFahrenheit(cel)
    else:
        far = int(input("Enter Temprature in Fahrenheit"))
        T.convertCelcius(far)
else:
    print("PLease Enter Valid Input")
#ques_4.
class MovieDetails:
    Mov=list()
    def __init__(self,artName,YoR,Rat):
        self.Aname=artName
        self.RelYear=YoR
        self.ratings=Rat
    def Add(self):
        self.NewMov={'Artist':self.Aname,'Release Year':self.RelYear,'Ratings':self.ratings}
        self.Mov.append(self.NewMov)
    def Display(self):
        for i in range(0,len(self.Mov)):
            print("The Artist of the Movie is {}".format(self.Mov[i]['Artist']))
            print("The Year of Release is {}".format(self.Mov[i]['Release Year']))
            print("The Ratings are {}".format(self.Mov[i]['Ratings']))

DDLJ=MovieDetails('ak','2006','5')
DDLJ.Add()
D3=MovieDetails('lewis','2014','2')
D3.Add()
D3.Display()
#ques_5.
class Animal:
    def animal_attribute(self):
        self.Color = 'black with white head'
        self.legs = 4
        self.Endangered = 'Endangered'
        print(self.Color, self.legs, self.Endangered, sep="\n")


class Tiger(Animal):
    def Yellow(self):
        pass


Tig = Tiger()
Tig.animal_attribute()
#ques_6.
#The Output of code Should be:-
# A A
# A B
#ques_7.
class Shape:
    __length=0
    __brdth=0
    def GetMeas(self):
        self.__length=int(input("Enter The Length Of the Shape "))
        self.__brdth=int(input("Enter The Breadth of the Shape "))
        return self.__length,self.__brdth
    def Area(self,leng,brd):
        self.Ar=leng*brd
        print(self.Ar)
class Rectangle(Shape):
    def __init__(self):
        pass
class Square(Shape):
    def __init__(self):
        pass

Sq=Square()
Rc=Rectangle()
sh=Shape()

ln,brd=sh.GetMeas()
if ln==brd:
    Sq.Area(ln,brd)
else:
    Rc.Area(ln,brd)


    
