"""
버블 정렬(Bubble Sort)이라는 이름은
정렬 과정에서 큰 값들이 마치 물속의 거품(bubble)처럼 위로 떠오르는 것처럼 보이기 때문에 붙여졌어요.
"""


def bubble_sort(numbers: list):
    for i in range(len(numbers)):
        swapped = False
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True

        if not swapped:  # 교환이 없으면 이미 정렬됨
            break

    return numbers


numbers = [4, 2, 6, 5, 1, 3]
bubble_sort(numbers)
print(numbers)


"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """
