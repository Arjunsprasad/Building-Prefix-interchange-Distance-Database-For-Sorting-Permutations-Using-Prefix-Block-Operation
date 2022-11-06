def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact =fact*i
    return fact

def stringvalue(n):
	if n==1:
		print("Invalid")
	elif n==2:
		value="12"
	elif n==3:
		value="123"
	elif n==4:
		value="1234"
	elif n==5:
		value="12345"
	else:
		print("Exceeded")
	return value

def twosorting(permute,fact):
    for i in range(0,fact):
        step=0
        originalper=["1","2"]
        if permute[i]=="12":
            print(permute[i]," ",step)
        else:
            step=step+1
            j=0
            p=list(permute[i])
            p[j], p[j+1]=p[j+1],p[j]
            if(p==originalper):
                print(permute[i]," ",step)


def thirdsorting(permute,fact,n,tempstorage):

    for i in range(0,fact):
        step=0
        originalper=["1","2","3"]
        if permute[i]=="123":
            print(permute[i]," ",step)
        else:
            p=list(permute[i])
            threemovea(p,originalper,step,permute[i],tempstorage)
            
def threemovea(p,originalper,step,permutation,tempstorage):
    p[0],p[1],p[2]=p[1],p[2],p[0]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        p[0],p[1],p[2]=p[2],p[0],p[1]
        threemoveb(p,originalper,step,permutation,tempstorage)
        
def threemoveb(p,originalper,step,permutation,tempstorage):
    p[0],p[1],p[2]=p[2],p[0],p[1]

    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        p[0],p[1],p[2]=p[1],p[2],p[0]
        threemovec(p,originalper,step,permutation,tempstorage)
    
def threemovec(p,originalper,step,permutation,tempstorage):
    p[0],p[2]=p[2],p[0]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        p[0],p[2]=p[2],p[0]
        threemoved(p,originalper,step,permutation,tempstorage)
    
def threemoved(p,originalper,step,permutation,tempstorage):
    p[0],p[1]=p[1],p[0]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        step=step+1
        if checking(p,tempstorage) == True :
            step=step+1
            print(permutation," ",step)
        else:
           threemovea(p,originalper,step,permutation,tempstorage) 
    
def checking(p,tempstorage):
    joining="".join(p)
    size=len(tempstorage)
    for i in range (0,size-1):
        if(joining==tempstorage[i]):
            return True
 
def foursorting(permute,fact,n,tempstorage):
    for i in range(0,fact):
        step=0
        originalper=["1","2","3","4"]
        if permute[i]=="1234":
            print(permute[i]," ",step)
        else:
            p=list(permute[i])
            fourmovea(p,originalper,step,permute[i],tempstorage)
            
def fourmovea(p,originalper,step,permutation,tempstorage):
    p[0],p[1],p[2],p[3]=p[1],p[2],p[3],p[0]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        if checking(p,tempstorage) == True :
            step=step+1
            print(permutation," ",step)
        else:
            p[0],p[1],p[2],p[3]=p[3],p[0],p[1],p[2]
            fourmoveb(p,originalper,step,permutation,tempstorage)
 
def fourmoveb(p,originalper,step,permutation,tempstorage):
    p[0],p[1],p[2]=p[1],p[0],p[2]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        if checking(p,tempstorage) == True :
            step=step+1
            print(permutation," ",step)
        else:
            p[0],p[1],p[2]=p[1],p[0],p[2]
            fourmovec(p,originalper,step,permutation,tempstorage) 

def fourmovec(p,originalper,step,permutation,tempstorage):
    p[0],p[1],p[2],p[3]=p[2],p[3],p[1],p[0]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        if checking(p,tempstorage) == True :
            step=step+1
            print(permutation," ",step)
        else:
            p[0],p[1],p[2],p[3]=p[3],p[2],p[0],p[1]
            fourmoved(p,originalper,step,permutation,tempstorage)
        
def fourmoved(p,originalper,step,permutation,tempstorage):
    p[0],p[3]=p[3],p[0]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        if checking(p,tempstorage) == True :
            step=step+1
            print(permutation," ",step)
        else:
            p[0],p[3]=p[3],p[0]
            fourmovee(p,originalper,step,permutation,tempstorage)

def fourmovee(p,originalper,step,permutation,tempstorage):
    p[0],p[2],=p[2],p[0]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        if checking(p,tempstorage) == True :
            step=step+1
            print(permutation," ",step)
        else:
            p[0],p[2]=p[2],p[0]
            fourmovef(p,originalper,step,permutation,tempstorage)

def fourmovef(p,originalper,step,permutation,tempstorage):
    p[0],p[1],p[2],p[3]=p[2],p[3],p[0],p[1]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        if checking(p,tempstorage) == True :
            step=step+1
            print(permutation," ",step)
        else:
            p[0],p[1],p[2],p[3]=p[2],p[3],p[0],p[1]
            fourmoveg(p,originalper,step,permutation,tempstorage)

def fourmoveg(p,originalper,step,permutation,tempstorage):
    p[0],p[1],p[2],p[3]=p[1],p[2],p[0],p[3]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        if checking(p,tempstorage) == True :
            step=step+1
            print(permutation," ",step)
        else:
            p[0],p[1],p[2],p[3]=p[2],p[0],p[1],p[3]
            fourmoveh(p,originalper,step,permutation,tempstorage)
        
def fourmoveh(p,originalper,step,permutation,tempstorage):
    p[0],p[1],p[2]=p[2],p[0],p[1]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        if checking(p,tempstorage) == True :
            step=step+1
            print(permutation," ",step)
        else:
            p[0],p[1],p[2]=p[1],p[2],p[0]
            fourmovei(p,originalper,step,permutation,tempstorage)

def fourmovei(p,originalper,step,permutation,tempstorage):
    p[0],p[1],p[2],p[3]=p[3],p[2],p[0],p[1]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        if checking(p,tempstorage) == True :
            step=step+1
            print(permutation," ",step)
        else:
            p[0],p[1],p[2],p[3]=p[2],p[3],p[1],p[0]
            fourmovej(p,originalper,step,permutation,tempstorage)
        
def fourmovej(p,originalper,step,permutation,tempstorage):
    p[0],p[1],p[2],p[3]=p[3],p[0],p[1],p[2]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        step=step+1
        if checking(p,tempstorage) == True :
            step=step+1
            print(permutation," ",step)
        else:
            if step<=4:
                fourmovea(p,originalper,step,permutation,tempstorage) 

def fivesorting(permute,fact,n,tempstorage):
  for i in range(0,fact):
        step=0
        originalper=["1","2","3","4","5"]
        if permute[i]=="12345":
            print(permute[i]," ",step)
        else:
            p=list(permute[i])
            fivemovea(p,originalper,step,permute[i],tempstorage)  
            
def fivemovea(p,originalper,step,permutation,tempstorage):
    p[0],p[1],p[2],p[3],p[4]=p[1],p[2],p[3],p[4],p[0]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        if checking(p,tempstorage) == True :
            step=step+1
            print(permutation," ",step)
        else:
            p[0],p[1],p[2],p[3],p[4]=p[4],p[0],p[1],p[2],p[3]
            fivemoveb(p,originalper,step,permutation,tempstorage)
        
def fivemoveb(p,originalper,step,permutation,tempstorage):
    p[0],p[1],p[2],p[3],p[4]=p[2],p[3],p[4],p[1],p[0]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        if checking(p,tempstorage) == True :
            step=step+1
            print(permutation," ",step)
        else:
            p[0],p[1],p[2],p[3],p[4]=p[4],p[3],p[0],p[1],p[2]
            fivemovec(p,originalper,step,permutation,tempstorage)
        
def fivemovec(p,originalper,step,permutation,tempstorage):
    p[0],p[1],p[2],p[3]=p[1],p[2],p[3],p[0]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        if checking(p,tempstorage) == True :
            step=step+1
            print(permutation," ",step)
        else:
            p[0],p[1],p[2],p[3]=p[3],p[0],p[1],p[2]
            fivemoved(p,originalper,step,permutation,tempstorage)
        
def fivemoved(p,originalper,step,permutation,tempstorage):
    p[0],p[1],p[2],p[3],p[4]=p[1],p[2],p[0],p[3],p[4]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        if checking(p,tempstorage) == True :
            step=step+1
            print(permutation," ",step)
        else:
            p[0],p[1],p[2],p[3],p[4]=p[2],p[0],p[1],p[3],p[4]
            fivemovee(p,originalper,step,permutation,tempstorage)
        
def fivemovee(p,originalper,step,permutation,tempstorage):
    p[0],p[1],p[2]=p[1],p[0],p[2]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        if checking(p,tempstorage) == True :
            step=step+1
            print(permutation," ",step)
        else:
            p[0],p[1],p[2]=p[1],p[0],p[2]
            fivemovef(p,originalper,step,permutation,tempstorage)

def fivemovef(p,originalper,step,permutation,tempstorage):
    p[0],p[1],p[2],p[3],p[4]=p[4],p[1],p[2],p[3],p[0]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        if checking(p,tempstorage) == True :
            step=step+1
            print(permutation," ",step)
        else:
            p[0],p[1],p[2],p[3],p[4]=p[4],p[1],p[2],p[3],p[0]
            fivemoveg(p,originalper,step,permutation,tempstorage)
        
def fivemoveg(p,originalper,step,permutation,tempstorage):
    p[0],p[2]=p[2],p[0]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        if checking(p,tempstorage) == True :
            step=step+1
            print(permutation," ",step)
        else:
            p[0],p[2]=p[2],p[0]
            fivemoveh(p,originalper,step,permutation,tempstorage)

def fivemoveh(p,originalper,step,permutation,tempstorage):
    p[0],p[1],p[2],p[3]=p[2],p[3],p[1],p[0]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
            p[0],p[1],p[2],p[3]=p[3],p[2],p[0],p[1]
            fivemovei(p,originalper,step,permutation,tempstorage)
        
def fivemovei(p,originalper,step,permutation,tempstorage):
    p[0],p[3]=p[3],p[0]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        if checking(p,tempstorage) == True :
            step=step+1
            print(permutation," ",step)
        else:
            p[0],p[3]=p[3],p[0]
            fivemovej(p,originalper,step,permutation,tempstorage)

def fivemovej(p,originalper,step,permutation,tempstorage):
    p[0],p[1],p[2],p[3],p[4]=p[3],p[4],p[1],p[2],p[0]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        if checking(p,tempstorage) == True :
            step=step+1
            print(permutation," ",step)
        else:
            p[0],p[1],p[2],p[3],p[4]=p[4],p[2],p[3],p[0],p[1]
            fivemovek(p,originalper,step,permutation,tempstorage)
        
def fivemovek(p,originalper,step,permutation,tempstorage):
    p[0],p[1],p[2],p[3],p[4]=p[2],p[3],p[4],p[0],p[1]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        if checking(p,tempstorage) == True :
            step=step+1
            print(permutation," ",step)
        else:
            p[0],p[1],p[2],p[3],p[4]=p[3],p[4],p[0],p[1],p[2]
            fivemovel(p,originalper,step,permutation,tempstorage)

def fivemovel(p,originalper,step,permutation,tempstorage):
    p[0],p[1],p[2]=p[2],p[0],p[1]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        if checking(p,tempstorage) == True :
            step=step+1
            print(permutation," ",step)
        else:
            p[0],p[1],p[2]=p[1],p[2],p[0]
            fivemovem(p,originalper,step,permutation,tempstorage)

def fivemovem(p,originalper,step,permutation,tempstorage):
    p[0],p[1],p[2],p[3],p[4]=p[3],p[4],p[2],p[0],p[1]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        if checking(p,tempstorage) == True :
            step=step+1
            print(permutation," ",step)
        else:
            p[0],p[1],p[2],p[3],p[4]=p[3],p[4],p[2],p[0],p[1]
            fivemoven(p,originalper,step,permutation,tempstorage)

def fivemoven(p,originalper,step,permutation,tempstorage):
    p[0],p[1],p[2],p[3]=p[2],p[3],p[0],p[1]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        if checking(p,tempstorage) == True :
            step=step+1
            print(permutation," ",step)
        else:
            p[0],p[1],p[2],p[3]=p[2],p[3],p[0],p[1]
            fivemoveo(p,originalper,step,permutation,tempstorage)

def fivemoveo(p,originalper,step,permutation,tempstorage):
    p[0],p[1],p[2],p[3],p[4]=p[4],p[2],p[3],p[0],p[1]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        if checking(p,tempstorage) == True :
            step=step+1
            print(permutation," ",step)
        else:
            p[0],p[1],p[2],p[3],p[4]=p[3],p[4],p[1],p[2],p[0]
            fivemovep(p,originalper,step,permutation,tempstorage)

def fivemovep(p,originalper,step,permutation,tempstorage):
    p[0],p[1],p[2],p[3]=p[3],p[2],p[0],p[1]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        if checking(p,tempstorage) == True :
            step=step+1
            print(permutation," ",step)
        else:
            p[0],p[1],p[2],p[3]=p[2],p[3],p[1],p[0]
            fivemoveq(p,originalper,step,permutation,tempstorage)
        
def fivemoveq(p,originalper,step,permutation,tempstorage):
    p[0],p[1],p[2],p[3]=p[3],p[0],p[1],p[2]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        if checking(p,tempstorage) == True :
            step=step+1
            print(permutation," ",step)
        else:
            p[0],p[1],p[2],p[3]=p[1],p[2],p[3],p[0]
            fivemover(p,originalper,step,permutation,tempstorage)
        
def fivemover(p,originalper,step,permutation,tempstorage):
    p[0],p[1],p[2],p[3],p[4]=p[3],p[4],p[0],p[1],p[2]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        if checking(p,tempstorage) == True :
            step=step+1
            print(permutation," ",step)
        else:
            p[0],p[1],p[2],p[3],p[4]=p[2],p[3],p[4],p[0],p[1]
            fivemoves(p,originalper,step,permutation,tempstorage)

def fivemoves(p,originalper,step,permutation,tempstorage):
    p[0],p[1],p[2],p[3],p[4]=p[4],p[3],p[0],p[1],p[2]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        if checking(p,tempstorage) == True :
            step=step+1
            print(permutation," ",step)
        else:
            p[0],p[1],p[2],p[3],p[4]=p[2],p[3],p[4],p[1],p[0]
            fivemovet(p,originalper,step,permutation,tempstorage)

def fivemovet(p,originalper,step,permutation,tempstorage):
    p[0],p[1],p[2],p[3],p[4]=p[4],p[0],p[1],p[2],p[3]
    if(p==originalper):
        step=step+1
        print(permutation," ",step)
        tempstorage.append(permutation)
    else:
        step=step+1
        if checking(p,tempstorage) == True :
            step=step+1
            print(permutation," ",step)
        else:
            if step<=5:
                fivemovea(p,originalper,step,permutation,tempstorage) 

def generatePermutations(value,start,end,permute):
    current=0
    if(start == end-1):
        permute.append(value)
        return permute
    else:
        for current in range(start,end):
            x = list(value)
            temp = x[start]
            x[start] = x[current]
            x[current] = temp
            
            generatePermutations("".join(x),start+1,end,permute)
            temp = x[start]
            x[start] = x[current]
            x[current] = temp
            
n = int(input("Enter a number: "))
fact= factorial(n)
permute = []
tempstorage = []
value = stringvalue(n)
print("All possible permutations and number of shortest moves to sort it : ")
generatePermutations(value,0,n,permute)
if n==2 : 
    twosorting(permute,fact)
elif n==3 :
    thirdsorting(permute,fact,n,tempstorage)
elif n==4 :
    foursorting(permute,fact,n,tempstorage)
elif n==5 :
    fivesorting(permute,fact,n,tempstorage)