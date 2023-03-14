work1 = lambda item: 'Вы ввели ноль' if item == 0 else 'Четное' if item % 2 == 0 else 'Нечетное'

work_2 = input("Введите любое число: ")

if not work_2.isnumeric():
    print("Введите пожалуйста число")

else:
    print(work1(int(work_2)))