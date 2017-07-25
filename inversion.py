
def mergesort(x):
    if len(x)<2:
        return x,0
    else:
        middle = int(len(x)/2)
        left,num1 = mergesort(x[:middle])
        right,num2 = mergesort(x[middle:])
        arr, num3 = mergeAndCount(left,right)
        return arr, num1+num2+num3

def mergeAndCount(x,y):
    result = []
    i = 0
    j = 0
    num = 0
    while i<len(x) and j<len(y):
        if x[i] <= y[j]:
            result.append(x[i])
            i += 1
        else:
            result.append(y[j])
            j += 1
            num += len(x)-i
    while i<len(x):
        result.append(x[i])
        i += 1
    while j<len(y):
        result.append(y[j])
        j += 1
    return result,num

total = 0
with open("/home/michael/Downloads/Integer.txt","r") as file:
    input = [int(x) for x in file.readlines()]
    print(mergesort(input))
print(total)


