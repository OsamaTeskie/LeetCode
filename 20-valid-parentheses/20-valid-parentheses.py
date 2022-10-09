class Solution:
    def isValid(self, s: str) -> bool:
        
        opens = "([{"
        closes = ")}]"
        
        current = []
        
        for i in s:
            if i in opens:
                current.append(i)
            else:
                if len(current) != 0:
                    if i == ")" and current[-1] == "(":
                        current.pop()
                    elif i == "]" and current[-1] == "[":
                        current.pop()
                    elif i == "}" and current[-1] == "{":
                        current.pop()
                    else:
                        break
                else:
                    return False
        if len(current) > 0:
            return False
        return True