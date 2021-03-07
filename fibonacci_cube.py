"""
 Generate a list of the first  fibonacci numbers,  being the first number. Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.

⌨️ Input (n): 5
🏆 Output: [0, 1, 1, 8, 27]
"""

from typing import List


def fibonacci(n: int) -> List[int]:
    # return a list of fibonacci numbers
    fibo_list = [0, 1]

    for i in range(n-2):
        next_number = fibo_list[i] + fibo_list[i+1]
        fibo_list.append(next_number)

    return fibo_list[0:n]


n = 3
# https://www.programiz.com/python-programming/methods/built-in/pow
print(list(map(lambda x: pow(x, 3), fibonacci(n))))
