def stringvalue(n):
    if (n < 10):
        value = "1"
        for i in range(2, n + 1):
            value = value + str(i)
        return value

def generatemoves(n):
    for i in range(1, n):
        for j in range(i, n + 1):
            for k in range(j + 1, n + 1):
                t = "0" + str(i) + str(j) + str(k)
                moves.append([0,i,j,k])

def generatePermutations(value, start, end, permute):
    current = 0
    if (start == end - 1):
        permute.append(value)
        return permute
    else:
        for current in range(start, end):
            x = list(value)
            temp = x[start]
            x[start] = x[current]
            x[current] = temp

            generatePermutations("".join(x), start + 1, end, permute)
            temp = x[start]
            x[start] = x[current]
            x[current] = temp

def tree(per,depth):
    temp=per
    maxdepth=(n//2)+1
    for move in moves:
        res = applymoves(temp, move)
        tmpres = res
        if depth==1:
            d1.append(res)
        elif depth==2:
            d2.append(res)
        elif depth==3:
            d3.append(res)
        elif depth==4:
            d4.append(res)
        elif depth==5:
            d5.append(res)
        else:
            d6.append(res)
        d = depth
        d = d + 1
        if d <= maxdepth:
            tree(tmpres, d)
    depth = 1

def Search():
    for i in range(1,len(permute)):
        for j in range(0,len(d1)):
            if permute[i]== d1[j]:
                k=str(permute[i])+" 1"
                file1.write(k)
                file1.write("\n")
                permute[i]=0
        for j in range(0,len(d2)):
            if permute[i]== d2[j]:
                k=str(permute[i])+" 2"
                file1.write(k)
                file1.write("\n")
                permute[i]=0
        for j in range(0,len(d3)):
            if permute[i]== d3[j]:
                k=str(permute[i])+" 3"
                file1.write(k)
                file1.write("\n")
                permute[i]=0
        for j in range(0,len(d4)):
            if permute[i]== d4[j]:
                k=str(permute[i])+" 4"
                file1.write(k)
                file1.write("\n")
                permute[i]=0
        for j in range(0,len(d5)):
            if permute[i]== d5[j]:
                k=str(permute[i])+" 5"
                file1.write(k)
                file1.write("\n")
                permute[i]=0
        for j in range(0,len(d6)):
            if permute[i]== d6[j]:
                k=str(permute[i])+" 6"
                file1.write(k)
                file1.write("\n")
                permute[i]=0

def applymoves(per,move):
    block1=""
    block2=""
    temp = per
    block1=temp[int(move[0]):int(move[1])]
    block2=temp[int(move[2]):int(move[3])]
    temp = temp.replace(block1, block2)
    length=len(temp)
    var=temp[0]
    temp=temp[1:length]
    temp=temp.replace(block2,block1)
    temp=var+temp
    return temp

file1 = open("output.txt","a")
file1.truncate(0)
d1,d2,d3,d4,d5,d6=[],[],[],[],[],[]
n = int(input("Enter a number: "))
moves = []
value = stringvalue(n)
permute=[]
generatemoves(n)
generatePermutations(value, 0, n, permute)
print(moves)
tree(value,1)
Search()
k=str(value)+" 0"
file1.write(k)
file1.close()
print("Completed")