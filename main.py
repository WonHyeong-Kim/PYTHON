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
n,m=map(int,input().split())
col=[]
max_number=0
for i in range(n):
  array=list(map(int, input().split()))
  min_number = 1000000
  for j in array:
    min_number=min(min_number,j) # 두 값중 제일 작은값 리턴
  max_number=max(max_number,min_number)
print(max_number)

# 1.
# input1 :  3 3
# input2 :  3 1 2
#           4 1 4
#           2 2 2
# output :  2

# 2.
# input1 :  2 4
# input1 :  7 3 1 8
#           3 3 3 4
# output :  3
