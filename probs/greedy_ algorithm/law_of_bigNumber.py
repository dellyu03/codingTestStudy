# 큰 수의 법칙 : 크기가 N인 배열이 주어질때 주어진 수들을 M번 더하여 가장 큰수를 만드는 법칙 단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없음
# 배열의 크기 N 숫자가 더해지는 횟수 M 그리고 K가 주어질때 
# 입력 조건 : 첫째 줄에 N(2<= N <= 1,000), M(1<= M <= 10,000), K(1<= K <= 10,000)인 자연수 각 자연수는 공백으로 구분
# 둘째 줄에 N개의 자연수가 주어지며 각 자연수는 공백으로 구분 단 각각의 자연수는 1이상 10,000이하
# 입력으로 주어지는 K는 항상 M보다 작거나 같다
# 입력 예시 5 8 3
#         2 4 5 4 6
# 출력 예시 : 46

n, m, k = map(int, input().split())
count = 0
plusTime = 0
answer = 0

numbers = list(map(int, input().split()))       #map 함수는 객체 값을 출력하기 때문에 list 형태로 바꾸어주어야 ㅎㅁ
numbers.sort(reverse=True)              #sort 함수는 결과로 None 값을 반환하기 때문에 변수에 담으면 안됨

first = numbers[0]
second = numbers[1]

while plusTime != m:
    for i in range(k):
        if plusTime == m:               #더하는 중간에 덧셈횟수가 m이 되는 것을 고려하지 않았었음
            break
        answer += first
        plusTime += 1
    for i in range(k):
        if plusTime == m:               #더하는 중간에 덧셈횟수가 m이 되는 것을 고려하지 않았었음
            break
        answer += second
        plusTime += 1

print(answer)
