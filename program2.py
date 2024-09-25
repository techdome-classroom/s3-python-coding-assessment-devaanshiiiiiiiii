class Solution(object):
    def romanToInt(self, s):
        Roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        Valid_combination=['IV','IX','XL','XC','CD','CM']
        val=0
        for i in range(len(Roman)):
            if Roman[i] not in Roman:
                return False 
            if i>0  and Roman[i-1:i+1] in Valid_combinations:
                val=Roman[Roman[i]]-Roman[Roman[i-1]]
                continue 
            if current> val:
                return False 
                val=current
            return True 
        pass



