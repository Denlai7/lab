import random
print(str(input())*2)  #1


w = input("word=")
for x in w:
    print(x+x,end="")   
    
n = input("введіть щось")[::-1]
print(n)
    
    
t=input("Enter txt:")
i=len(t)
while(i>0):
    i = i-1                 #2
    print(t[i], end="")


sheep = True
while sheep:
    a = int(input("first num "))
    b = int(input("second num "))
    bun = "Do you want to continue? yes/no "
    slay = "nah bestie, it is not giving, retry"
    bob = (str(input("What do you want to do? + - * / ")))
    if bob == "+":
        print(a + b)
        bam1 = (str(input( bun )))    #3
        if bam1 == "yes":
            continue
        elif bam1 == "no":
            sheep = False
    elif bob == "-":
        print(a - b)
        bam2 = (str(input( bun )))
        if bam2 == "yes":
            continue
        elif bam2 == "no":
            sheep = False
    elif bob == "/":
        if a == 0:
            print(slay)
            continue
        elif b == 0:
            print(slay)
            continue
        else:
            print(a/b)
            bam2 = (str(input( bun )))
            if bam2 == "yes":
                continue
            elif bam2 == "no":
                sheep = False
    elif bob == "*" :
        print(a * b)
        bam1 = (str(input( bun )))   
        if bam1 == "yes":
            continue
        elif bam1 == "no":
            sheep = False
            
aaa = input("введіть дію ділення")
try:
    exec(aaa)
except ZeroDivisionError:
    print("it is not dividingguu bestie")
except:
    print("Something happened...")
else:
    print(aaa)
    

for i in range(5):
    x=random.randint(0, 100)
    print(x)
