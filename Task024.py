# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, 
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растёт N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора 
# на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним. Напишите программу для нахождения 
# максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед 
# некоторым кустом заданной во входном файле грядки.


def enter_num(text):
    try:
        a = int(input(f"Enter the {text} :> "))
    except:
        print("Error! This is not integer number!")
    return a

def we_grow_berries(n):
    berries = []
    for i in range(n+2):
        if i < n:
            berries.append(enter_num(f'number of berries per bush {i+1}'))
        else:
            berries.append(berries[i - n])
    return berries
    
def sum_and_max(n, berries):
    sum = []
    for i in range(n):
        sum.append(berries[i] + berries[i+1] + berries[i+2])
    maximum = max(sum)
    return maximum

def task():
    n = enter_num('number of bushes')
    berries = we_grow_berries(n)
    maximum = sum_and_max(n, berries)
    print('The maximum number of berries that the collecting module')
    print(f'can collect in one run is:>  {maximum}')
    

task()

