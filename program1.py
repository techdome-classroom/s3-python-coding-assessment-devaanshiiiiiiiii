class Solution(object):
    def isValid(self, s):
        Stack=[]
        DataBrackets={'[':']','{':'}','(':')'}
        for i in s:
            if i in DataBrackets.values():
                Stack.append(i)
            elif i in DataBrackets.values():
                if Stack and Stack[-1]== DataBrackets[i]:
                    stack.pop()
                else:
                    return False
            else:
                return False 
        return not Stack
        







    



  

