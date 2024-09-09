
l=[]
def remove_items():
    l.pop(b)
def add_to_list():
    r=True
    while (r):
    
        w=input("\nenter things to be done in here:")
        l.append(w)

        print("\ndo you have more to add?")
        n=input("\nenter y to continue, n to stop:")
        x=n.lower()
        if x=="y":
            r=True
        else:
            r=False
            print("--TO DO--\n")
            f=1
            for i in l:
                print(f,".",i)
                f=f+1
add_to_list()
r=True
while r:
    c=input("\nhave you completed any of the work?(y/n):")
    ch=c.lower()
    if ch=="y":
        global z
        z=int(input("\nenter the number of task completed:"))
        b=z-1
        remove_items()
        f=1
        for i in l:
            print(f,".",i)
            f=f+1
        if len(l)==0:
            print("good work, all works done!!\n")
            break
        
    elif ch=="n":
        
        for i in l:
            print(f,".",i)
            f=f+1
        r=False
