"""
Problem: Given an array of integers nums, find all the duplicates in the array using a hash table (dictionary).
"""


def find_duplicates(list):
    hash_table = {}
    result = []

    for item in list:
        if item in hash_table:
            hash_table[item] += 1
            if hash_table[item] >= 1:
                result.append(item)
        else:
            hash_table[item] = 1

    return result


"""
# 중복 찾기 알고리즘 최적화 정리

## 원본 코드의 문제점
- `hash_table[item] >= 1` 조건이 항상 참 (이미 += 1 했으므로)
- 같은 값이 여러 번 나타나면 중복으로 계속 추가됨

## 최적화 방법 비교

### 1. Set 방법 (속도 최적화)
```python
seen = set()
duplicates = set()
# ...
return list(duplicates)
```
- **장점**: 가장 빠름, 자동 중복 제거
- **단점**: `list(duplicates)` 변환 시 메모리 추가 사용

### 2. Dictionary Flag 방법 (메모리 최적화)
```python
hash_table = {}
result = []
# flag로 첫 중복만 추가
```
- **장점**: 메모리 효율적 (list 변환 불필요)
- **단점**: Set보다 약간 느림

## 결론
- **시간복잡도**: 둘 다 O(n)
- **공간복잡도**: 
  - Set: O(n + 2k) - set과 list 모두 저장
  - Dict Flag: O(n + k) - **메모리 적게 사용**
- **속도**: Set 방법이 더 빠름
- **선택**: 중복이 많으면 Dict Flag, 적으면 Set 추천
"""
"""
# using set
def find_duplicates(list):
    seen = set()
    duplicates = set()

    for item in list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return list(duplicates)

# using flag
def find_duplicates(list):
    hash_table = {}
    result = []

    for item in list:
        if item in hash_table:
            if not hash_table[item]:  # 처음 중복 발견 시에만
                result.append(item)
                hash_table[item] = True
        else:
            hash_table[item] = False

    return result
"""
