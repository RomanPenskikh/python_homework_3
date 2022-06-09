# Составить список простых множителей натурального числа N
print('укажите натуральное число N')
digit_N = int(input())
list_N = [(i) for i in range(2, digit_N+1) if ((i % 2) == 0)]
digit_min_N = min(list_N)
list_N_array = []
digit_N_2 = int(digit_N/digit_min_N)
while digit_N_2 != 0:
    list_N_array.append(digit_N_2)
    list_N = [(j) for j in range(2, digit_N_2+1) if ((j % 2) == 0)]
    digit_N_2 = int(digit_N_2/digit_min_N)
print(f'Список простых множителей натурального числа {digit_N} {list_N_array}')
