# 12. В списке, состоящем из вещественных элементов, вычислить:
# 1) количество элементов списка, лежащих в диапазоне от А до В;
# 2) сумму элементов списка, расположенных после максимального элемента.
# Упорядочить элементы списка по убыванию модулей элементов.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    arr = [1, 2, 3, -4, 15, 16, 17, 24, 23, -3]
    a = int(input("Введите а: "))
    b = int(input("Введите b: "))
    counter = 0

    for i in arr:
        if a < i < b:
            counter += 1
    print(counter)
    print(sum(arr[arr.index(max(arr))+1 : ]))
    arr.sort(key=abs, reverse=True)
    print(arr)