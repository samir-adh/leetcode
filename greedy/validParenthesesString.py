# we will have a counter 'stack' that will emulate a stack
# and 'error' that will count the errors
# and 'wildcards' that will count '*'
# if we encounter '(' we increase stack
# if we encounter ')'
#   if stack > 0 we decrease stack
#   else we increase errors
# if we encounter '*' we increase wildcards
# at the end we add stack to errors
# we return errors <= wildcards
class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        wildcards = []
        for i,c in enumerate(s):
            if c == '(':
                stack.append(i)
            if c == ')':
                if stack:
                    stack.pop()
                elif wildcards:
                    wildcards.pop()
                else:
                    return False
            if c == '*':
                wildcards.append(i)
        while stack and wildcards and stack[-1] < wildcards[-1]:
            stack.pop()
            wildcards.pop()
        return len(stack) == 0
        

# a * can only be used as ')' if  the  stack > 0
# a * can only be used as '(' if is is before a ')'