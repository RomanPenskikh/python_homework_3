# Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]
from array import array
from pstats import SortKey
from unittest.util import sorted_list_difference


array_digit = [1, 2, 3, 5, 1, 5, 3, 10]
array_digit.sort()
array_digit.append(array_digit[1])
array_t = array_digit
array_digit_2 = []

for i in range (0, len(array_digit)-1):
        if array_t[i] != array_t[i+1]:
            array_digit_2.append(array_t[i])

        
print(array_digit)
print(array_digit_2)

