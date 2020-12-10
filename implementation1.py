# implementation1
# my
n=input()
planer=input().split()
x=1
y=1
n=int(n)
for i in planer:
  if i == 'R':
    temp=y+1
    if temp <n:
      y=temp
  elif i == 'L':
    temp=y-1
    if temp > 1:
      y=temp
  elif i == 'U':
    temp = x-1
    if temp > 1:
      x = temp
  elif i == 'D':
    temp = x+1
    if temp < n:
      x = temp

print(x,y)
#book
n=int(input())
x,y=1,1
plans=input().split()
dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_type=['L','R','U','D']

for plan in plans:
  for i in range(len(move_type)):
    if plan == move_type[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  if nx<1 or ny <1 or nx>n or ny>n:
    continue
  x=nx
  y=ny
print(x,y)
# input1 : 5
# input2 : R R R U D D
# output : 3 4