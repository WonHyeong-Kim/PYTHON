#greedy
#my
N=1260
sum+=N//500
sum += (N%500)//100
sum += ((N%500)%100)//50
sum += (((N%500)%100)%50)//10

print(sum)
###################################
#book
N=1260
coin_type=[500,100,50,10]
sum=0

for coin in coin_type:
  sum+=N//coin
  N=N%coin

print(sum)