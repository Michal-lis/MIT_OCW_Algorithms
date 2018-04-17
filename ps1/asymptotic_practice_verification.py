from prettytable import PrettyTable
from math import *


# first group
def f11(n):
    return pow(n, 0.9999999) * log2(n)


def f12(n):
    return 1000000 * n


def f13(n):
    return pow(1.000001, n)


def f14(n):
    return pow(n, 2)


# second group
def f22(n):
    return pow(2, 100000 * n)


def f23(n):
    return (n - 1) * n / 2


def f24(n):
    return n * pow(n, 0.5)


def calculate_for_10(function):
    return function(10)


def calculate_for_100(function):
    return function(100)


def calculate_for_10000(function):
    return function(10000)


def calculate_for_1000000(function):
    return function(1000000)


t = PrettyTable(['argument', 'pow(n, 0.9999999) * log2(n)', '1000000 * n', 'pow(1.000001, n)', 'pow(n, 2)'])
t.add_row(['n=10'] + (list(map(int, list(map(calculate_for_10, [f11, f12, f13, f14]))))))
t.add_row(['n=100'] + (list(map(int, list(map(calculate_for_100, [f11, f12, f13, f14]))))))
t.add_row(['n=10000'] + (list(map(int, list(map(calculate_for_10000, [f11, f12, f13, f14]))))))
t.add_row(['n=1000000'] + (list(map(int, list(map(calculate_for_1000000, [f11, f12, f13, f14]))))))
print(t)
