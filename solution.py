class Solution:
    def romanToInt(self, s: str) -> int:
        map={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        result=0
        for i in range(len(s)-1):
            if map[s[i]]>=map[s[i+1]] and i!=len(s)-1:
                result+=map[s[i]]
            else:
                result-=map[s[i]]
        result+=map[s[-1]]
        return result


 