#greedy3
#my
n,m=map(int,input().split())
col=[]
for i in range(n):
  array=list(map(int, input().split()))
  col.append(min(array))

max_number = max(col)
print(max_number)
#book

# 1.
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# 2.
# 2 4
# 7 3 1 8
# 3 3 3 4