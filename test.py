#w = input("word=")
#for x in w:
#    print(x+x)   
    
    
        
#n = input("введіть щось")[::-1]
#print(n)
    
#ZeroDivisionError

aaa = input("введіть дію ділення")
try:
    exec(aaa)
except ZeroDivisionError:
    print("it is not dividingguu bestie")
except:
    print("Something happened...")
else:
    print(aaa)