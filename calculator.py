#task_001

num1=float(input("enter the number:"))
num2=float(input("enter the number:"))
print("press 1 for add ")
print("press 2 for sub")
print("press 3 for multiply ")
print("press 4 for divide") 
choice=int(input("enter your choice:"))
if(choice==1):
    print(num1+num2)
elif(choice==2):
    print(num1-num2)
elif(choice==3):
    print(num1*num2)
elif(choice==4):
    print(num1/num2)
else:
    print("syntax error")