
"""
Find a maximum power of two that divides a given number N
Input
858616
Output
8
"""
n = 858616
print(n & (~(n - 1)))