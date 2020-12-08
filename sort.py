# sort 비교
from random import randint
import time

array = []
for _ in range(1000):
    array.append(randint(1, 100))  # 1~100사이 랜덤수

# for a in range(len(array)):
#  print(array[a])
start_time = time.time()

for i in range(len(array)):
    min = i
    for j in range(i + 1, len(array)):
        if array[min] > array[j]:
            min = j
    array[min], array[i] = array[i], array[min]  # swap

end_time = time.time()

print("수행시간", end_time - start_time)

array = []
for _ in range(1000):
    array.append(randint(1, 100))  # 1~100사이 랜덤수

start_time = time.time()
array.sort()
end_time = time.time()

print("수행시간", end_time - start_time)