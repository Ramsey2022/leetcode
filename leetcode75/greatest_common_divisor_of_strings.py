"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

#Example

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
"""

#if string 1 + string 2 == string 2 + string 1 
#   find longest common substring
#Else return ''

from math import gcd

def gcdOfStrings(self, str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ''
    else:
        return str1[:gcd(len(str1), len(str2))]