class Solution:
    # def __init__(self):
    #     self.q=deque()

        

    # def Push(self, x: int) -> None:
    #     # self.push(x)
    #     self.q.append(x)

        

    # def Pop(self) -> int:
    #     for i in range(len(self.q)-1):
    #         self.q.append(self.q.popleft())
    #     return self.q.popleft()

    # def isValid(self, s: str) -> bool:
    #     d=Solution()
    #     for c in s:
    #         if c in "({[": #c == '(' or c == '{' or c == '[': 
    #             d.Push(c)
    #         else:
    #             if len(d.q) == 0:
    #                 return False

    #             ch = d.Pop()
    #             if (c == ')' and ch == '(') or (c == ']' and ch == '[') or (c == '}' and ch == '{'):
    #                 continue
    #             else:
    #                 return False
    
    #     return len(d.q) == 0
    def isValid(self, s: str) -> bool:
        d=[]
        for c in s:
            if c in "({[": #c == '(' or c == '{' or c == '[': 
                d.append(c)
            else:
                if len(d) == 0:
                    return False

                ch = d.pop()
                if (c == ')' and ch == '(') or (c == ']' and ch == '[') or (c == '}' and ch == '{'):
                    continue
                else:
                    return False
    
        return len(d) == 0

        