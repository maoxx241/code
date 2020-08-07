class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # stack = string segments for outStr, cur = current string segment
        stack, cur = [], ''
        for c in s:
            if c == '(':
                # add current string segment to stack, cos we're now at new stack
                stack += [cur]
                cur = ''
            elif c == ')':
                # since segments are only added via '(', this means that the previous segment was preceded by a '('
                if stack:
                    cur = stack.pop() + '(' + cur + ')' 
            else:
                cur += c
        
        # add all the string segments together
        while stack:
            cur = stack.pop() + cur
        
        return cur
    