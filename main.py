"""a=8
b=8
print("A") if(a>b) else print("=") if(a==b) else print("B")"""


"""marks=[98,99,97,90]
for index,mark in enumerate (marks):
    if(index==3):
        print("harry awesome")"""


"""import math
a=math.sqrt(9)
print(a)"""


"""from math import ceil
a=ceil(8.34)
print(a)"""

"""from math import floor as f
a=f(8.3435)
print(a)"""


'''import math
print(dir(math))'''


'''import os
if not os.path.exists("data"):
    os.mkdir("data")
    for i in range (1,100):
        os.mkdir(f"data/day{i+1}")

import os
for i in range(1,100):
    os.rename(f"data/day{i+1}",f"data/tutorial{i+1}")



    

import os

folders = os.listdir("data")
print(folders)

for folder in folders:
    print(os.listdir(f"data/{folder}"))



import os
folders=os.listdir("data")
print(os.getcwd())


import os

print(os.getcwd())
os.chdir("C://")
print(os.getcwd())


x=20
def hello():
    global x
    x=4
    y=5
    print(y)
    print("local x",x)
hello()
print("global x",x)


f=open('myfile.txt','r')
text=f.read()
print(text)
f.close()


            

with open ("myfile.txt","a") as f:
    f.write("hey janvi")



cube =lambda x: x*x*x
print(cube(5))


def cube(x):
    return(x*x*x)
l=[2,3,4,5]
newl=list(map(cube,l))
print(newl)  


def filter_function(a):
    return a>2
l=[2,3,4,5,6]
newl=list(filter(filter_function,l))
print(newl)                   


from functools import reduce
l=[2,3,4,5,6]  
def mysum(x,y):
    return(x+y)
sum=reduce(mysum,l)
print(sum)



class person :
    name = "prerit"
    occupation = "student"
    age=18
    def info(self):
        print(f"my name is {self.name} and i am {self.age} and my occupation is {self.occupation}")
obj=person()
obj.info()
                                                                                                                                                                                                                 

class  prerit:
    def __init__(self,n,o):
        self.name= n
        self.occ=o
    def info(self):
     print(f"{self.name} is a {self.occ}")
a=prerit("janvi","docter")
b=prerit("prerit","engineer")
print(a.info())  
print(b.info())     






def greet(fx):
    def mfx():
        print("Good morning")
        fx()
        print("Thank you for using")
    return mfx

@greet 
def hello():
    print("sir")

hello()




def greet(fx):
    def mfx(*args, **kwargs):
        print("Good morning")
        result = fx(*args, **kwargs)  
        print("Thank you for using")
        return result
    return mfx

@greet
def add(a, b):
    print(a + b)
    return a + b   

result = add(2, 5)
print( result)

class Myclass:
 def __init__(self,value):
 
  self._value=value
 def show(self):
  print(f"value is {self._value}")
 @property

 def tenvalue(self):
   return 10*self._value
obj=Myclass(10)
print(obj.tenvalue)
obj.show()

class Myclass:
 def __init__(self,value):
  self._value=value

 def show(self):
  print(f"value is {self._value}")

 @property
 def ten_value(self):
   return 10*self._value
 
 @ten_value.setter
 def ten_value(self,newvalue):
        self._value=newvalue/10

obj=Myclass(10)
obj.ten_value=67
print(obj.ten_value)
obj.show()


class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def detail(self):
        print(f"name  of employee:{self.id},{self.name}")
class Program(Employee):
      def language(self):
       print("the default language  is python")
e1=Program("prerit",234)    
e1.detail()

                   
class Employee:
    def __init__(self):
        self.name="prerit"
a=Employee()
print(a.name)


class employee:
    def __init__(self):
        self.__name="prerit"
a=employee()

print(a._employee__name)


class Student:
    def __init__(self):
     self._name="prerit"

    def _funcname(self):
       return "code"
    
class Subject(Student):
   pass

obj=Student()
obj1=Subject()
print(obj._name)
print(obj._funcname())
print(obj1._name)
print(obj1._funcname())


class Student:
    def __init__(self):
        self._name = "Prerit"

    def _funName(self):
        return "code"

class Subject(Student):  
    pass


obj = Student()
obj1 = Subject()

print(obj._name)         
print(obj._funName())  
print(obj1._name)        
print(obj1._funName()) 


class Method:
    @staticmethod
    def add(a,b):
        return a+b
result=Method.add(2,4)
print(result)


class Employee:
    compname="apple"
    def __init__(self,name):
        self.name=name
        self.raiseamt=0.2
    def showdetail(self):
        print(f"the name of employee is {self.name} and the raise amount in {self.compname}  is {self.raiseamt}")
emp1=Employee("prerit")
emp1.raiseamt=1.2
emp1.showdetail()
emp2=Employee("janvi")
emp2.compname="meta"
emp2.showdetail()



class employee:
    company="apple"
    def show(self):
        print(f"the  name of employee is {self.name} and  the company is {self.company}")
    @classmethod
    def changecompany(cls,newcompany) :
        cls.company=newcompany
e1=employee()
e1.name="prerit"
e1.changecompany("tesla")
e1.show()

       
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])
e1=employee("harry",1200000)
print(e1.name)
print(e1.salary)
string="john-144444"
e2=employee.fromStr(string)
print(e2.name)
print(e2.salary)                  




class Parentclass:
    def parent_method(self):
        print("this is the parent method")

class childclass(Parentclass):
    def parent_method(self):
        print("harry")
        super().parent_method()

    def child_method(self):
        print("this is the child method")
        super().parent_method()

child_object = childclass()
child_object.child_method()
child_object.parent_method()


class employee:
    name="prerit"
    def __len__(self):
        i=0
        for c in self.name:
          i=i+1
        return i
a=employee()
a.name
print(len(a))




from emp import employee
e=employee("prerit")
print(e)



class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def area(self):
        return self.x * self.y

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)
        
    def area(self):
        return 3.14 * super().area()

radii = Circle(5)
print(radii.area())


class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    def __add__(self,x):
       return vector(self.i+x.i,self.j+x.j,self.k+x.k)
a=vector(2,3,4)
b=vector(4,5,6)
print(a)
print(b)
print(a+b)
print(type(a+b))


class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def makesound(self):
        print("sound mde by the animal")
class dog(animal):
    def __init__(self,name,breed):
        animal.__init__(self,name,species="carnivores")
        self.breed=breed
    def makesound(self):
        print("bark")
d=dog("dod","bulldog")    
d.makesound()
a=animal("dog","carnivores")  
a.makesound()




class animal:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"name is {self.name}")
class dance:
    def __init__(self,dance):
        self.dance=dance
    def show(self):    
        print(f"dance is {self.dance}")
class animaldance(dance,animal):
    def __init__(self,dance,name):
        self.name=name
        self.dance=dance
o=animaldance("kathak","tom")
print(o.name)
print(o.dance)
o.show()



class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def show(self):
        print(f"name:{self.name}")
        print(f"species:{self.species}")
class dog(animal):
    def __init__(self,breed,name):
        animal.__init__(self,name,species="dog")
        self.breed=breed
    def show(self):
        print(f"breed : {self.breed}")
class golden(dog):
    def __init__(self,name,color):
        dog.__init__(self,name,breed="golden")
        self.color=color
    def show(self):
            dog.show(self)
            print(f"color:{self.color}")
o=golden("tom","red")
o.show()


import time
time.sleep(10)
print(4)
print("print after 10 sec")



import requests
import argparse



def download_file(url,local_filename):
    local_filename = url.split('/')[-1]
    
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                 
                f.write(chunk)
    return local_filename

parser =argparse.ArgumentParser()
parser.add_argument("url",help="url of file")
parser.add_argument("output",help=" by which name save  the file")
args=parser.parse_args()
print(args.url)
print(args.output)
download_file(args.url, args.output)



numbers=[2,3,4,5,6,10,7,18,1]
while(n:=len(numbers))>0:
    print(numbers.pop())



import shutil
shutil.copy("main.py","main2.py")


import shutil
import os
os.remove("tur/file.file")



import requests
# response=requests.get("https://www.google.com")
# print(response.text)


url="https://jsonplaceholder.typicode.com//posts"

data={
  "title":'prerit',
  "body":'janvi',
  "userid":1403
}
headers={
    'content-type': 'application/json; charset=UTF-8',
}
response=requests.post(url,headers=headers , json=data)
print(response.text)




def mygenerators():
  for i in range(30):
    yield i

gen=mygenerators()
# print(next(gen))
# print(next(gen))
for j in gen:
  print(j)


from  functools import lru_cache
import time
@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5
print(fx(5))
print("done for 5")
print(fx(20))
print("done for 20")
print(fx(50))
print("done for 50")

print(fx(5))
print("done for 5")'''



# import re
# pattern= r"[A-Z]+ivil"
# text='''(August 1, 1816 – March 21, 1862) was an American lawyer,
#  politician and soldier. A peacetime lawyer, Slack served in the Missouri General
#    Assembly from 1842 to 1843 and saw combat in the Mexican–American War. After the
#      outbreak of the American Civil War in April 1861, Slack,
#  who held pro-slavery views, supported the Confederate cause. When Sivil
#    the Missouri State Guard was formed the next'''

# match=re.search(pattern,text)
# print(match)
'''matches=re.finditer(pattern,text)
for match in matches:
    print(match)
# print(type(match.span()))
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])




import threading
import time
def func(seconds):
    print(f"sleeping for {seconds} seconds")

    time.sleep(seconds)
time1=time.perf_counter()
#func(4)
#func(2)
#func(10)


t1=threading.Thread(target=func,args=[4])
t2=threading.Thread(target=func,args=[2])
t3=threading.Thread(target=func,args=[10])
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

time2=time.perf_counter()
print(time2-time1)


import multiprocessing
import requests
def downloadfile(url,name):
    response=requests.get(url)
    open(f"file{name}.jpg",
    "wb").write(response.content)

url="https://picsum.photos/2000/3000"
pros=[]
for i in range(5):
    p=multiprocessing.Process(target=downloadfile,args=[url,i])
    p.start()
    pros.append(p)

for p in pros:
        p.join()'''


def vow:
vowel='a,e,i,o,u,A,E,I,O,U'

