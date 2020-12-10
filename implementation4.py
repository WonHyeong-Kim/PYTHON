#implementation4
#my

#n,m = map(int,input().split())
n,m=4,4
#x,y,direction = map(int,input().split())
x,y,direction =1, 1, 0
arr=[]

# for i in range(n):
#     arr.append(list(map(int,input().split())))
arr=[[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
move=0
dCheck=0
d_temp=direction

while True:
    cx=x
    cy=y
    bx = x
    by = y
    if direction == 0:#북
        cy-=1
        d_temp=3
        bx+=1
    elif direction == 1:#동
        cx-=1
        d_temp = 0
        by -= 1
    elif direction == 2:#남
        cy+=1
        d_temp = 1
        bx -= 1
    elif direction == 3:  # 서
        cx+=1
        d_temp = 2
        by += 1

    if 1<=cx and cx<=4 and 1<=cy and cy<=4:
        if arr[cx][cy] == 0:#육지
            x=cx
            y=cy
            move+=1
            dCheck =0
            arr[cx][cy]=1
            continue
    if dCheck==4:# back
        if 1>bx or bx>4 or 1>by or by>4:#뒤가 바다
            break
        else:
            x=bx
            y=by
            dCheck = 0
            continue
    dCheck += 1
    direction = d_temp

print(move)



#book
n,m = map(int,input().split())
d = [[0]*m for _ in range(n)] # n x m => 0 리스트
x,y,direction = map(int,input().split())
d[x][y] = 1
array=[]
for _ in range(n):
    array.append(list(map(int,input().split())))
# 북0 동1 남2 서3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction-=1
    if direction == -1:
        direction=3

move = 1
d_check=0
while True:
    turn_left()
    cx = x + dx[direction]
    cy = y + dy[direction]
    if d[cx][cy] == 0 and array[cx][cy] ==0:
        d[cx][cy]=1
        x = cx
        y = cy
        move+=1
        d_check=0
        continue
    else:
        d_check+=1

    if d_check ==4:
        cx = x - dx[direction]
        cy = y - dy[direction]

        if array[cx][cy]==0:
            x=cx
            y=cy
        else:
            break
        d_check=0

print(move)
#input : 4 4
#        1 1 0
#        1 1 1 1
#        1 0 0 1
#        1 1 0 1
#        1 1 1 1
#output : 3