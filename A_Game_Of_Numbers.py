def GameOfNo(A=[]):
    N = len(A)-1
    result = []
    status = True
    for i in range(N):
        q = i+1
        while q <= N:
            if A[i] < A[q]:
                r = q+1
                while r <= N:
                    if A[q] > A[r]:
                        status = False
                        result.append(A[r])
                        break
                    else:
                        r += 1
                break
            else:
                q += 1
                status = True
        if status:
            result.append(-1)
    result.append(-1)
    return result

item = [3, 7, 1, 7, 8, 4, 5, 2]
print(GameOfNo(item))