import time
t=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
hour=int(input("enter the hour:"))
if(0<hour<12):
    print("good morning") 
elif(12<hour<15):
    print("good afternoon")
elif(17<hour<19):
    print("good evening ")
elif(19<hour<24):
    print("good night")
else:
    print("erorr")




    
