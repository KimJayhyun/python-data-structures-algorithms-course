"""
매 단계마다 "선택"하기 때문이에요:

1. 정렬되지 않은 부분에서 최솟값을 "선택"
2. 그걸 정렬되지 않은 부분의 맨 앞과 교환
3. 이 과정을 반복
"""


def selection_sort(numbers: list):
    for i in range(len(numbers)):
        min_value = numbers[i]
        min_index = i
        for j in range(i + 1, len(numbers)):
            value = numbers[j]

            if min_value > value:
                min_value = value
                min_index = j

        if not i == min_index:
            numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    return numbers


print(selection_sort([4, 2, 6, 5, 1, 3]))


"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """
