#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 26. Из списка целых чисел составить три других, в первый из которых записать числа, кратные
# 5, во второй - числа, кратные 7, а в третий - остальные числа.


if __name__ == '__main__':
    a = [1, 2, 3, 4, 15, 16, 17, 21, 14, 23]
    five = []
    seven = []
    other = []
    for i in a:
        if i % 5 == 0:
            five += [i]
        elif i % 7 == 0:
            seven += [i]
        else:
            other += [i]
    print(five, seven, other)

    five_lc = [i for i in a if not(i % 5)]
    seven_lc = [i for i in a if not(i % 7)]
    other_lc = [i for i in a if (i % 5 and i % 7)]
    print(five_lc, seven_lc, other_lc)
