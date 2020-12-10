# implementation2
# my
n=int(input())
count=0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if j %10 == 3 or (int(j /10) ==3 and j !=33) or k %10 == 3 or (int(k/10)==3 and k!=33) or i%10==3:
                count+=1

print(count)

# book
n=int(input())
count=0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count+=1

print(count)