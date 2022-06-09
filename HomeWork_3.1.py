# Найти НОК двух чисел
print('укажите первое число')
digit_1=int(input())
print('укажите второе число')
digit_2=int(input())

list_1=[(digit_1*i) for i in range(1, digit_1+1)]
print(list_1)
list_2=[(digit_2*i) for i in range(1, digit_2+1)]
print(list_2)
digit_min=min(digit_1,digit_2)
list_min=[]
k=0
for i in range(1,digit_min):
    for j in range(digit_min-1):
        if list_1[i]==list_2[j]:
            list_min.append(list_1[i])
print(list_min)
list_min_digit=min(list_min)
print(list_min_digit)


