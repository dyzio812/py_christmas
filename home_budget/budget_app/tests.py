from django.test import TestCase
from datetime import date, timedelta
import calendar

# Create your tests here.

# def zeros(n):
#     i = 1
#     total = 0
#     while 5**i <= n:
#         total += (n // (5**i))
#         i += 1
#     return total
#
#
# print(zeros(1000))
# # total = [n//5**i for i in range]


# def solution(n):
#     return sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)
#
#
# print(solution(10))

# a = datetime.date(2000, 2, 1) - datetime.timedelta(days=1)
# print(a)

b = date.today().replace(month=+1, day=1) - timedelta(1)
print(b)