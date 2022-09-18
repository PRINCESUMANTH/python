'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

'''
class Solution(object):
    def isValid(self, s):
        count=0
        if len(s)%2==0 or len(s)==1:
            pass
        else:
            return False
        for i in range (len(s)):
            
            if s[i]=="(":
                if s[i+1]==")":
                    count=1
                else:
                    count=0
            if s[i]=="{":
                if s[i+1]=="}":

                    count=1

                else:

                    count=0
            if s[i]=="[":

                if s[i+1]=="]":

                    count=1

                else:

                    count=0
            if count==1:
                return True 
            else :
                return False
t=Solution ()
print (t.isValid("[][]"))

