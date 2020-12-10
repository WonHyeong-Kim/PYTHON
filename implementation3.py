#implementation3
#my
input = input() # 문자열 리턴
row_first = int(ord(input[0])-ord('a')+1)
col_first = int(input[1])
dx=[1, -1, 2, -2]
dy=[1, -1, 2, -2]
count=0
result=[]
for i in dx[0],dx[1]:

    for j in dy[2],dy[3]:
        row = row_first
        col = col_first
        row = row + i
        col = col + j
        if 1<=row<=8 and 1<=col<=8:
            if str(row)+str(col) not in result:
                count+=1
                result.append(str(row)+str(col))
for k in dx[2],dx[3]:
    for m in dy[0],dy[1]:
        row = row_first
        col = col_first
        row = row + k
        col = col + m
        if 1<=row<=8 and 1<=col<=8:
            if str(row)+str(col) not in result:
                count+=1
                result.append(str(row)+str(col))
print(count)
#book
input = input()
col_first = int(ord(input[0])-ord('a')+1)
row_first = int(input[1])
steps = [(-2,-1),(-2,1), (2,-1), (2,1), (1,-2), (1,2), (-1,2), (-1,-2)]

count=0
result=[]
for step in steps:
    row = row_first + step[0]
    col = col_first + step[1]
    if 1<=row<=8 and 1<=col<=8:
        if str(row)+str(col) not in result:
            count+=1
print(count)

#input : a1
#ouput : 2