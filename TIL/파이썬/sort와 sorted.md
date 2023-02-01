# sort와 sorted

> ### [1. sort 함수](#1-sort-ed95a8ec8898-1)  
> ### [2. sorted 함수](#2-sorted-ed95a8ec8898-1)

## 1. sort 함수
- 리스트를 정렬하는 함수 
- 튜플, 딕셔너리, 문자열에는 사용불가
- 형태 
```py
listName.sort()
listName.sort(key = function(), reverse = bool)
```

- 반환 값은 None (원본 리스트를 수정하며 변수에 리스트.sort()값을 저장하면 none 값이 됨)

오름차순 배열
```py
list = [5, 1, 2, 4, 3]
list.sort()
# list = [1, 2, 3, 4, 5]
```

내림차순 배열
```py
list = [5, 1, 2, 4, 3]
list.sort(reverse = True)
# list = [5, 4, 3, 2, 1]
```

<br>

## 2. sorted 함수
- sort처럼 리스트를 정렬하는 함수임
- 리스트 안의 값이 문자열이여도 정렬 가능
- 형태 = sorted(리스트)
- 반환 값은 정렬된 리스트(원본 리스트를 변형하지 않으므로 변수에 값을 넣어줘야 정렬된 리스트를 사용할 수 있음)

```py
list = ['b', 'a', 'c', 'd', 'e']
newList = sorted(list)
# newList = ['a', 'b', 'c', 'd', 'e']

list = [5, 1, 2, 4, 3]
newList = sorted(list)
# newList = [1, 2, 3, 4, 5]
```

딕셔너리 객체도 받을수 있음
```py
dict = {1: 'a', 3:'c', 2:'b'}
newDict = sorted(dict)
# newDict = [1, 2, 3]
```

sorted 값에 딕셔너리를 받을때
