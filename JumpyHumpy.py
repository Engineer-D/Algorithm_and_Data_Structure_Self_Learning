def jumpyHumpy(size, arr = [],):
    arrSize = len(arr)
    stamina = []
    strength = 0
    
    if size != arrSize:
        return -1
    
    for i in range(arrSize):
        strength = strength^arr[i]
        nextPos = i+1
        pos = i
        while nextPos < arrSize:
            if arr[pos] < arr[nextPos]:
                strength = strength ^ arr[nextPos]
                pos = nextPos
                nextPos += 1
                
            else:
                nextPos += 1
    
        stamina.append(strength)
        strength = 0
    return max(stamina)

size = int(input())
item = [int(x) for x in input().split()]
print(jumpyHumpy(size, item))