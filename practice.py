#practices


'''sum=0
print("prerit general store")
while (True):
    
    userInput=input( "enter the item price or press q to quit ")
    if(userInput!='q'):
        sum=sum+int(userInput)
        
    else:
      print(f"the total bill is {sum}.thanks for shopping with  us")
    break'''


'''def factorial(num):
 if(num==0):
    return 1
 else:
    return num*factorial(num-1)
fact=factorial(5)
print("the factorial is " ,fact)'''





# import math
# num = int(input("enter the number:"))
# sr=math.sqrt(num)
# print(sr)   




# b=int(input("enter the base"))
# h=int(input("enter the height"))
# area=0.5*(b+h)
# print(area)




# x=13
# y=6
# temp=x
# x=y
# print("x=",x)
# y=temp
# print("y=",y)



# distance=float(input("enter the distance in km"))
# dm=distance*0.625
# print(dm,"mile")




# num=int(input("enter the number="))
# if(num==0):
#     print("zero")
# else:
#     if(num<0):
#         print("negative")
#     else:
#         print("positive")





# num=int(input("enter the  number="))
# if(num%2==0):
#     print("even")
# else:
#     print("odd")




# year=int(input("enter the year:"))
# if(year%4==0):
#     print("leap year")
# else:
#     print("not a leap year")




# a=4
# b=5
# c=54
# if(a>b and a>c):
#     print("a")
# elif(b>a and b>c):
#     print("b")
# elif(a==b or b==c or c==a):
#     print("equal")
# else:
#     print("c")

    



# num =int(input("enter the number ="))
# for i in range(2,num):
#     if(num%i==0):
#         print("not a prime")
#         break
#     else:
#         print("PRIME")
#         break
    




import random
num=random.randint(1,7)
print(num)





# lower = int(input("Enter the lower bound: "))
# upper = int(input("Enter the upper bound: "))

# for num in range(lower, upper + 1):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)





# num=4
# for i in range(1,11):
#     print(num,"*",i,"=",num*i)





# num=int(input("enter the number"))
# a=0
# b=1
# print(a)
# print(b)
# for i in range(0,num):
#     c=a+b
#     a=b
#     b=c
#     print(c)






# lower = int(input("Enter the lower limit: "))
# upper = int(input("Enter the upper limit: "))

# for num in range(lower, upper):
#     temp = num
#     n = len(str(num))
#     sum = 0  # Renamed the variable to avoid conflict
#     while temp > 0:
#         digit = temp % 10
#         cube = digit ** n
#         sum=sum+ cube
#         temp=temp//10
#     if num == sum:
#         print(num)





# num=int(input("enter the  number "))
# if(num<0):
#     print("enter the psitive nummber")
# else:
#     sum=0
#     while num > 0:
#         sum=sum+num
#         num=num-1
# print(sum)





# nterms=int(input("enter the no of terms:"))
# new=list(map(lambda x: x*x*x,range(nterms)))
# # print(new)

# for i in range(nterms):
#     print(new[i])




# for i in  range(1,100):
#     if i%13 == 0:
#         print(i)




# decimal = int(input("enter the number here"))
# print(hex(decimal),"in hexadecimal")
# print(oct(decimal),"in octal")
# print(bin(decimal),"in binary")




# char=input("enter the charcter")
# print("ascii value of",char,"is",ord(char))




# def findhcf(x,y):
#     if x>y:
#         smaller=y
#     else:
#         smaller=x
#     for i in range(1,smaller+1):
#             if(x%i==0 and  y%i==0):
#                 hcf=i
#     return hcf
                
# print(findhcf(8,16))






# def fact(num):
#     for i in range(1,num+1):
#         if(num%i==0):
#          print(i)
# fact(10)




# import random, itertools
# deck=list(itertools.product( range(1,14),["spade","diamond","club","heart"]))
# random.shuffle(deck)
# print(deck)




"""import calendar
year =int(input("enter year-"))
month=int(input("enter month-"))

cal=calendar.month(year,month)
print(cal)
"""