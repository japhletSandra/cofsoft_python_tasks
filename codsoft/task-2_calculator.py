def add(u1,u2):
    return u1+u2
def sub(u1,u2):
    if u1>u2:
        c=u1-u2
    else:
        c=u2-u1
    return c
def mul(u1,u2):
    return u1*u2
def div(u1,u2):
    return u1/u2
def rem(u1,u2):
    return u1%u2

r=True
while (r):
    user_input1=eval(input("enter 1st number:"))
    user_input2=eval(input("enter 2nd number:"))
    print("operations:\n1.add\n2.subtract\n3.multiply\n4.divide\n5.reminder\n")
    ch=int((input("enter your choice(1/2/3/4):")))
    if ch==1:
        print("addition:",add(user_input1,user_input2))
        
    elif ch==2:
        print("subtraction:",sub(user_input1,user_input2))
               
    elif ch==3:
        print("multiplication:",mul(user_input1,user_input2))
        
    elif ch==4:
        print("division:",div(user_input1,user_input2))
        
    elif ch==5:
        print("reminder:",rem(user_input1,user_input2))
    
    else:
        print("invalid choice")
    print("do you want to continue?")
    n=input("enter y to continue, n to stop:")
    x=n.lower()
    if x=="y":
        r=True
    else:
        r=False
