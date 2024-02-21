'''Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.'''

from self import self

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if(haystack==needle):
            return 0
        elif (len(needle) > len(haystack)):
            return -1
        else:
            for i in range(0, len(haystack)):
                substring=""

                if(i+len(needle)<=len(haystack)):
                    for j in range(i,i+len(needle)):
                        substring=substring+haystack[j]

                    print(substring)
                    if(substring==needle):
                        return i
                else:
                    return -1

            return -1


    haystack = input("Enter Haystack: ")
    needle = input("Enter Needle: ")

    print("The index of first occurrence is: ", strStr(self,haystack, needle))