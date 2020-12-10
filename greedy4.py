#greedy4
#my
n, k = map(int,input().split())

count =0
while True:
  if n%k == 0:
    n=n/k
    count+=1
  else:
    n-=1
    count+=1
  if n ==1:
    break

print(count)

#book
n, k = map(int,input().split())

count =0
while True:
  target = (n//k)*k # 24        나누어 떨어질 수를 구한다.
  count+=(n-target) # 1         나누어 떨어질 수까지의 차이를 더한다.
  n=target          # 24

  if n<k:          # 1 < 3       나누는 수보다 작아지는 경우는 1일 경우뿐.
    break
  n//=k            # 나눈다.
  count+=1         # 나눌때 마다 더한다.
print(count-1)

# input  : 25 5
# output : 2