""" 
Reformat the String
Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).
You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.
Return the reformatted string or return an empty string if it is impossible to reformat the string.
Example 1:
Input: s = "a0b1c2"
Output: "0a1b2c"
Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
Example 2:
Input: s = "leetcode"
Output: ""
Explanation: "leetcode" has only characters so we cannot separate them by digits.
Example 3:
Input: s = "1229857369"
Output: ""
Explanation: "1229857369" has only digits so we cannot separate them by characters.
Example 4:
Input: s = "covid2019"
Output: "c2o0v1i9d"
Example 5:
Input: s = "ab123"
Output: "1a2b3
"""
import operator
from itertools import zip_longest
from functools import reduce


def reformat(s):
    alphas, digits = list(map(list, (zip(
        *list(map(list, zip_longest([c for c in s if c.isalpha()], [c for c in s if c.isdigit()])))))))
    print(alphas, digits)

    nonsense = [x for x in (
        list(reduce(operator.add, zip(alphas, digits)))) if x != None]

    print(nonsense)

    if nonsense[-1].isdigit() and nonsense[-2].isdigit() or nonsense[-1].isalpha() and nonsense[-2].isalpha():
        return ''
    else:
        return ''.join(nonsense)


print(reformat("a0b1c2"))
print(reformat("leetcode"))
print(reformat("1229857369"))
print(reformat("covid2019"))
print(reformat("ab123"))
