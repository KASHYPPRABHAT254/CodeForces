n = int(input())
h = list(map(int,input().split(' ')))
count = 0
for i in range(n):
    count+=1
    for j in range(i+1,n):
        if(j==n-1):
            for m in range(0,i):
                if(h[m]<h[n-1] and h[i]>h[m]):
                    count+=1
            break
        elif(h[j]<h[j+1] and h[i]>h[j]):
            count+=1
        else:
            break
print(count)
