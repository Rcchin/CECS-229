#another way of adding vectors
def addn(v,w):return [v[i]+w[i] for i in range(len(v))]
#input should be addn([2,3],[3,5])
# will display [5,8]
flag = True
print("This program will add 2 vectors")


#a.find(",")
#a.split(",")

#while loop to get input
while(flag):
    #gets input
    a = (input("Enter first vector"))
    #uses delimeter to get values if no comma jumps to else for error trap
    if(a.find(",") != -1):
        #puts vector in array
        v= a.split(",")
        

        #used to jump out of loop
        flag = False
    
    else:
        print("Error retry")
#resets for second input follows same format as first
flag = True
while(flag):
    b = (input("Enter second vector"))
    if(b.find(",") != -1):
        w = b.split(",")
        flag = False
    
    
    else:
        print("Error retry")
    
#converts string int so you can add
for i in range(len(v)):
    v[i] = (int)(v[i])
    w[i] = (int)(w[i])
#calls function to add vectors
print(addn(v,w))


    



    

      
