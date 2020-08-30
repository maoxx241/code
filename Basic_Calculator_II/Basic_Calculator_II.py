class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return "0"
        stack=[]
        cur=0
        sign='+'
        for i in range(len(s)):
            ch=s[i]
            
            if ch.isdigit():
                cur=cur*10+int(ch)
            if ch in '+-*/' or i ==len(s)-1:
                if sign=="+":
                    stack.append(cur)
                if sign=="-":
                    stack.append(-cur)
                if sign=="*":
                    stack.append(stack.pop()*cur)
                if sign=="/":
                    p = stack.pop()
                    res=abs(p)//cur
                    stack.append(res if p>=0 else -res)
                
                cur=0
                sign=ch
        return sum(stack)
                