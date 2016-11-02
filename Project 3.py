def scalar_vector_mult(alpha, v):
    return[alpha*v[i] for i in range(len(v))]
flag = True

while(flag):
    #gets input
    a = (input("Enter the vector"))
    #uses delimeter to get values if no comma jumps to else for error trap
    if(a.find(",") != -1):
        #puts vector in array
        v = a.split(",")
        

        #used to jump out of loop
        flag = False
    #if input is not a vector you will be asked to input another value
    else:
        print("Error retry")
#This while loop is to error check the alpha value
while True:
    try:
        alpha = int(input("Enter a number to multiply the vector by"))
        break
    except ValueError:
        print("Error not valid number! Please try again: " )
    
    
#converts string int so you can add
for i in range(len(v)):
    v[i] = (int)(v[i])

    
#calls function to add vectors
print(scalar_vector_mult(alpha,v))
