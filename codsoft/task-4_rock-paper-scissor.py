import  random as rn
print("lets play stone paper scissors")

n=int(input("choose number of turns [5/10/20]:"))
i=0
op_options=["stone","paper","scissors"]
y=['wonderful','great choice','I\'ll win the next round','watch your back','let me win!!']
x=rn.choice(op_options)
score=0
m_score=0
while i<=n:
    user_choice=input("enter your choice:")
    print(x)

    if user_choice==x:
        print("tie")
    elif user_choice=="stone" and x=="scissors":
        print(rn.choice(y))
        score+=1

    elif user_choice=="scissors" and x=="paper":
        print(rn.choice(y))
        score +=1
    elif user_choice=="paper" and x=="stone":
        print(rn.choice(y))
        score +=1   
    else:
        print('I scored this one,better luck next time')
        m_score+=1
    i+=1
print("you scored:",score)
print("I scored :",m_score)
if score==m_score:
    print("tie")
elif score>m_score:
    print("you won!!")
else:
    print("i won")