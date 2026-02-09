"""
카드 정리하는 것과 똑같아요:
손에 카드를 한 장씩 받으면서 정렬한다고 상상해보세요:

1. 첫 카드는 그냥 둠
2. 두 번째 카드를 받아서 적절한 위치를 찾아 "삽입"
3. 세 번째 카드를 받아서 적절한 위치를 찾아 "삽입"
4. 반복...
"""


def insertion_sort(numbers: list):
    for i in range(1, len(numbers)):
        current_value = numbers[i]
        current_index = i

        j = i - 1
        while j >= 0:
            # 값들을 뒤로 밀어냄 (swap이 아님)
            if current_value < numbers[j]:
                numbers[current_index] = numbers[j]
                current_index = j
                j -= 1
            else:
                break

        numbers[current_index] = current_value

        print(numbers)

    return numbers


print(insertion_sort([4, 2, 6, 5, 1, 3]))


"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """
