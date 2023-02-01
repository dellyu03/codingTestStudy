# 거스름돈으로 줄 500원, 100원, 50원, 10원 짜리 동전이 무한히 존재
# 거스름돈이 N원일때 거슬러 줘야 할 동전의 최소 개수를 구하시오
# 단 거슬러줘야 할 돈 N은 항상 10의 배수

n = int(input())

count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin
print(count)




        


