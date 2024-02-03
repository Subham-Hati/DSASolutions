"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

https://leetcode.com/problems/longest-common-prefix/description/
"""

class Solution(object):
    def longestCommonPrefix(strs):
        outputLongestCommonprefix = ""
        lengthOfInputList = len(strs)
        characterFlag = True
        firstString = strs[0]

        for stringValue in strs:
            if(len(stringValue)<len(firstString)):
                firstString=stringValue

        if (lengthOfInputList == 1):
            outputLongestCommonprefix=strs[0]
        elif (lengthOfInputList != 0):

            for characterIndex in range (0,len(firstString)):

                for listElements in range(0,lengthOfInputList):

                    if(firstString[characterIndex]!= (strs[listElements])[characterIndex]):
                        characterFlag=False
                        break

                if(characterFlag==True):
                    outputLongestCommonprefix+=firstString[characterIndex]
                else:
                    break

        return outputLongestCommonprefix;

    inputSize = int(input("Enter input list size: "))
    inputList=[]
    for i in range(0, inputSize):
        inputList.append(input("Enter a string: "))

    print("Input List: ", inputList)

    commonPrefix=longestCommonPrefix(inputList)

    if(commonPrefix==""):
        print("There is no common prefix among the input strings.")
    else:
        print("Longest Common Prefix: ", commonPrefix)

    #print(longestCommonPrefix(["flower","flow","flight"]))