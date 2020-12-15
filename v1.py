def knapsack():
    print("---------------------------------------------------------------------") 
    totalWeight = int(input("Enter the total weight: "))
    count = int(input("How many variables are there?: "))

    weights = list(map(int,input("Enter weights (seperated by a space): ").split()))
    values = list(map(int,input("Enter values (seperated by a space): ").split()))

    weights.insert(0,0) 
    values.insert(0,0)
  
    T = []
    rows = len(weights)
    columns = totalWeight+1   
    for i in range(rows):
        inner = []
        for j in range(columns):
            if(i == 0):
                inner.append(0)
            elif(weights[i] > j):
                inner.append(T[i-1][j])
            else:
                inner.append(max(values[i] + T[i-1][j-weights[i]], T[i-1][j]))
        T.append(inner)

    path = findpath(T, weights, totalWeight)
    path.reverse()
    printFunc(T, path)

def knapsack2():
    print("---------------------------------------------------------------------") 
    totalWeight = int(input("Enter the total weight: "))
    count = int(input("How many variables are there?: "))

    weights = list(map(int,input("Enter weights (seperated by a space): ").split()))
    values = list(map(int,input("Enter values (seperated by a space): ").split()))

    weights.insert(0,0) 
    values.insert(0,0)
  
    T = []
    rows = len(weights)
    columns = totalWeight+1   
    for i in range(rows):
        inner = []
        for j in range(columns):
            if(i == 0):
                inner.append(0)
            elif(weights[i] > j):
                inner.append(T[i-1][j])
            else:
                mult = j//weights[i]
                maxVal = T[i-1][j]
                for k in range(mult+1):
                    maxVal = max(values[i]*k + T[i-1][j-weights[i]*k], maxVal)
                inner.append(maxVal)
        T.append(inner)

    path = findpath2(T, weights, values, totalWeight)
    path.reverse()
    printFunc(T, path)


def findpath(T, weights, totalWeight):
    maxVal = [T[len(weights)-1][totalWeight]]
    path = [[len(weights)-1, totalWeight]]
    
    done = False
    count = 0
    while(not(done)):
        x = path[count][0]
        y = path[count][1]
        if(T[x][y] == 0):
            done = True
            break
        else:
            if(T[x-1][y] == T[x][y]):
                path.append([x-1,y])
            else:
                path.append([x-1,y-weights[x]])
        count+=1
    return path


def findpath2(T, weights, values, totalWeight):
    maxVal = [T[len(weights)-1][totalWeight]]
    path = [[len(weights)-1, totalWeight]]
    
    done = False
    count = 0
    while(not(done)):
        x = path[count][0]
        y = path[count][1]
        if(T[x][y] == 0):
            done = True
            break
        else:
            if(T[x-1][y] == T[x][y]):
                path.append([x-1,y])
            else:
                mult = y//weights[x]
                for k in range(mult):
                    if(T[x-1][y-weights[x]*(k+1)] + values[x]*(k+1) == T[x][y]):
                        path.append([x-1,y-weights[x]*(k+1)]) 
        count+=1
    return path

def printFunc(T, path):
    print("---------------------------------------------------------------------") 
    print("Final Table:")
    for i in range(len(T)):
        print(T[i])
    print("Final Path:")
    for i in range(len(path)):
        print(path[i])
    

def main():
    while True:
        try:
            program = int(input("Enter '0' for knapsack {0,1}, enter '1' for non-negative knapsack: "))
        except ValueError:
            print("Wrong type, enter an integer.")
            continue
        
        if(program!=0 and program!=1):
            print("Wrong input, enter a '0' or a '1'.")
            continue 
        else:
            break
    
    if(program):
        knapsack2()
    else:
        knapsack()
main()








