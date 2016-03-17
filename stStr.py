'''

Find Substring
For a given source string and a target string, you should output the first index(from 0) of target string in source string.

If target does not exist in source, just return -1.

Example:
If source = "source" and target = "target", return -1.
If source = "abcdabcdefg" and target = "bcd", return 1.

'''



class Solution:
    def strStr(self, source, target):
        # if the source string does not meet the requirement, return -1
        
        if target == None or source == None:
            return -1
        
        if len(target) == 0:
            return 0
    
        for i in range(len(source)-len(target) +1):
            for j in range(len(target)):
                
                if source[i+j] != target[j]:
                    break
                elif j == len(target) - 1:
                    return i
        
        return -1
