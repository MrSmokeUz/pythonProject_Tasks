#Task #1
from django.db.models.expressions import result
from requests_toolbelt.multipart.encoder import total_len

# I will give you an integer. Give me back a shape that is as long and wide as the integer. The integer will be a whole number between 1 and 50.

q = 5
n = 15
c = "+"
b = '     '
for x in range(q):
        n = n - 2
        b = b + ' '
        print(b+c*n)

# Task #2 create  a yolka
q = 5
n = 1
c = "+"
b = ' ' * q

for x in range(q):
    print(b + c * n)
    b = b[:-1]
    n += 2


# Task #3 replace with alphabet position

def alphabet_position(text):
    for x in text:
        print(ord(x))

alphabet_position('Hello')

#task #4 Complete the square sum function so that it squares each number passed into it and then sums the results together.

# For example, for [1, 2, 2] it should return 9 because 12+22+22=91^2 + 2^2 + 2^2 = 912+22+22=9.

def square_sum(numbers):
    return sum(i**2 for i in numbers)

square_sum([1,2,2])


# Task #5 You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.
# a can contain numbers or strings. x can be either.
# Return true if the array contains the value, false if not.

#solution 1
def check(seq, elem):
    if elem in seq:
        return True
    else:
        return False

check([1,7,8],5)

#solution 2
def check(seq,elem):
    return elem in seq



# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24


def grow(arr):
    result = 1
    for x in arr:
        result *= x  # Умножаем каждый элемент на результат
    return result  # Возвращаем результат

# Пример использования
print(grow([1, 2, 3]))  # Вывод: 6

# Given an array of integers, return a new array with each value doubled.
#
# For example:

# 1, 2, 3] --> [2, 4, 6]

def maps(a):
    for x in range(len(a)):
        a[x] *= a[x]
        return a


print(maps([1,2,4]))




