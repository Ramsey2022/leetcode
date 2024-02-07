"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
def reverseString(self, s: List[str]) -> None:
    x = len(s) - 1
    i = 0
    while i < x:
        s[i], s[x] = s[x], s[i]
        x -= 1
        i += 1
        
        
# OR s.reverse()