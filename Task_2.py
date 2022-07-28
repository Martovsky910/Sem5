import random
count = 0
sum = 2021
while sum > 0:
    count +=1
    if sum%2 == 0:
        computer = random.randint(1,28)
        print(computer, ':Конфет поставил компьютер')
        sum -= computer
        print(f'Сумма оставшихся конфет:', sum)
        if sum <= 0:
            print('Победил компьютер')
    else:
        user = int(input('Введите количество конфет, которое возьмете от 1 до 28 \n'))
        if user > 28 or user <1:
            print('Неккоректное число')
            exit(0)
        print(user, ':Конфет поставил пользователь')
        sum -= user
        print(f'Сумма оставшихся конфет:',sum)
        if sum <= 0:
            print('Победил пользователь') 
