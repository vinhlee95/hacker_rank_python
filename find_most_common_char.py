"""
Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

https://www.hackerrank.com/challenges/most-commons/problem
"""

s = "aabbbccde"

"""
First approach: manual count 🐌🐌🐌
"""
char_list = [char for char in s]
unique_char_list = list(set(char_list))

result = []
for char in unique_char_list:
    count = 0
    for character in s:
        if character == char:
            count += 1
    result.append((char, count))
    count = 0

result.sort(key=lambda item: (-item[1], item[0]))
for index, item in enumerate(result):
    if index <= 2:
        print(item[0], item[1])

"""
Second approach: count using Counter 🏎🏎🏎
"""
from collections import Counter

chars = Counter(s).items()

for char, count in sorted(chars, key=lambda item: (-item[1], item[0]))[:3]:
    print(char, count)

"""
3rd approach: using class 🤯🤯🤯
"""
from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass


[print(*c) for c in OrderedCounter(sorted(s)).most_common(3)]
