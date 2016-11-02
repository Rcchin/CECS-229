#-------------------------------------------
#CECS 229 Project 1
#Addition Algorithm

#This program implements Algorithm 2 page 251 of Roxen txt.
#-------------------

#Setting for algorithm
c = 0
#-------------------

print("This program has 2 binary numbers using an algorithm.")
print("You will be prompted to enter 2 binary numbers separately")

#Requesting input
array1  = list((input("Input the first binary number")))
array2  = list((input("Input the second binary number")))

#Formats binary number from array
userin1 = ''.join(str(e) for e in array1)
userin2 = ''.join(str(e) for e in array2)

print(userin1)
print("+")
print(userin2)

#The algorithm requires that the binary numbers to be entered in reverse
array1.reverse()
array2.reverse()


#Below determines the length of the binary numbers entered
while(len(array1) != len(array2)):
    if(len(array1)> len(array2)):
       array2 = array2+[0]
    
    else:
       array1 = array1 + [0]


#Time to add
s=[0]*(len(array1)+1)

for i in range(len(array1)):
    d = (int(array1[i]) + int(array2[i]) + c)//2
    s[i] = int(array1[i])+int(array2[i])+ c - 2*d
    c=d
    s[len(array1)]=c
s.reverse()
result = ''.join(str(e) for e in s)
print(result)

#from class
#s = [0]*(len(array1)+1)
#for i in range(len(array1)):
    #d = (int(array1[i]+ int(array2[i]+c)//2
    #s[i] = int (array1[i] + int(aray2[i] + c -(2*d)
    #c=d
    #s[len(array1)] =c
#s.reverse
#result =  ''.join(str(e) for e in s)
#print result
       
