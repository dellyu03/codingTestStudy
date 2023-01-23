# split 함수

- 파이썬의 함수
- 인자에 구분자와 분할 횟수를 넣어 구분자를 기준으로 문자열을 분할 횟수 만큼 분할함
- 구분자와 분할 횟수는 필수 인자는 아님

## split 함수의 형태
> split 함수를 쓸때 구분자와 분할 횟수는 필수가 아님  
> 단, split함수에 아무 인자가 없으면 공백을 기준으로 문자열을 분할함
```python
문자열.split() #공백을 기준으로 문자열 분리
문자열.split('구분자', 분할 횟수) #구분자를 기준으로 분할횟수 만큼 문자열 분할
```

ex)
```py
greet = "Hello world"
a, b = geet.split()
print(a)                #Hello가 출력됨
print(b)                #world가 출력됨
```


## split 함수 활용 
- 파이썬에서는 한번에 여러개의 변수에 각각 다른 값을 넣어줄 수 있음
- split 함수를 이용해서 쪼갠 문자열을 한번에 각각 다른 변수에 넣는 것이 가능
```python
a, b = ("Hello World").split() #a에는 Hello가 b에는 World가 들어가게 됨
print(a)
print(b)
# 실행 결과 : Hello
#           World 
```

