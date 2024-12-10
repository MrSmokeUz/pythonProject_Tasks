#Task #1
from pydoc import replace

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
        result *= x
    return result


print(grow([1, 2, 3]))

# Given an array of integers, return a new array with each value doubled.
#
# For example:

# 1, 2, 3] --> [2, 4, 6]

def maps(a):
    for x in range(len(a)):
        a[x] *= a[x]
        return a


print(maps([1,2,4]))

# TASK #8
# Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').
# Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').
# Create a function which translates a given DNA string into RNA.
# "GCAT"  =>  "GCAU"


# Solution 1
def dna_to_rna(dna):
    if 'T' in dna:
       c = dna.replace('T','U')
       print(c)

# Solution 2
def dna_to_rna(dna):
    return dna.replace("T", "U")

dna_to_rna('TTTT')



# TASK #9

# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0. Your function only needs to return the result, what is shown between parentheses in the example below is how you reach that result and it's not part of it, see the sample tests.
# 2 -> 3 (1 + 2)
# 8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)



# solution 1
def summation(num):
    return sum( i for i in range(1,num + 1))

# solution 2
def summation(num):
    return sum(range(1,num+1))

summation(2)


# TASK 10
# You get an array of numbers, return the sum of all of the positives ones.

def positive_sum(arr):
    if not arr:
        return 0
    return sum(x for x in arr if x > 0)

print(positive_sum([1, -4, 7]))

#TASK 11 Write a function which converts the input string to uppercase.
def make_upper_case(s):
    return s.upper()

#TASK 12 This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

def simple_multiplication(number):
    if number%2== 0:
       return number * 8
    else:
       return number * 9

print(simple_multiplication(2))

#TASK 13 Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

# solution 1
def get_grade(s1, s2, s3):
    a = ((s1+s2+s3)/3)
    if a >= 90 and a <= 100:
        return 'A'
    elif a>=80 and a <=90:
        return 'B'
    elif a>=70 and a <=80:
        return 'C'
    elif a>=60 and a <=70:
        return 'D'
    elif a>=0 and a <=60:
        return 'F'

# solution 2
def get_grade(s1, s2, s3):
    return {6: 'D', 7: 'C', 8: 'B', 9: 'A', 10: 'A'}.get((s1 + s2 + s3) / 30, 'F')

# solution 3
scores = {10: 'A', 9: 'A', 8: 'B', 7: 'C', 6: 'D'}

def get_grade(*args):
    mean = sum(args) / len(args)
    return scores.get(mean // 10, 'F')

    # return "F"

print(get_grade(5,4,3))


# Your task is to create a function that does four basic mathematical operations.
#
# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.
# Examples(Operator, value1, value2) --> output


#solution 1
def basic_op(operator, value1, value2):

    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2

# solution 2
def basic_op(operator, value1, value2):
    return eval(str(value1) + operator + str(value2))

