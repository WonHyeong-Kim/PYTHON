#greedy2
#my
N=5 #배열 요소 수
M=8 #총 개수
K=3 #반복가능
array=[2,4,5,4,6]

array.sort()
array.reverse()
sum=0
count=0

for _ in range(M):
  if count >= 2:
    sum+=array[1]
    count=0
  else:
    sum+=array[0]
    count+=1

print(sum)
######################
#book
n, m, k = map(int, input().split()) # input으로 받은 3문자를 split()함수로 공백을 기준으로 list로 나눈다.
                                    # 이를 int변수에 넣어 그 결과값을 리턴하여 n, m, k에 넣는다.
array=list(map(int, input().split())) #map의 결과는 list가 아니라 list로 변경.
array.sort()
first_number = array[n-1] #가장 큰수
second_number = array[n-2]

sum=0;
while True:
  for i in range(k):
    if m==0:
      break
    sum+=first_number
    m-=1
  if m == 0:
    break
  sum += second_number
  m -= 1

print(sum)
#book2 - 연산횟수 줄임
n, m, k = map(int, input().split()) # input으로 받은 3문자를 split()함수로 공백을 기준으로 list로 나눈다.
                                    # 이를 int변수에 넣어 그 결과값을 리턴하여 n, m, k에 넣는다.
                                    # 5 8 3
array=list(map(int, input().split())) #map의 결과는 list가 아니라 list로 변경.
                                      # 2 4 5 4 6
array.sort()
first_number = array[n-1] #가장 큰수
second_number = array[n-2]

sum=0;
sum = first_number * k * (m//(k+1)+m%(k+1))
sum += second_number * (m//(k+1))

print(sum)
