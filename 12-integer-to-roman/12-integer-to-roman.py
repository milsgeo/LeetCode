class Solution:
    def intToRoman(self, num: int) -> str:
        lookup_int={
            "I":1,
            "IV":4,
            "V":5,
            "IX":9,
            "X":10,
            "XL":40,
            "L":50,
            "XC":90,
            "C":100,
            "CD":400,
            "D":500,
            "CM":900,
            "M":1000
        }
        
        res=""
        output=[]
        
        for k,v in reversed(lookup_int.items()):
            while num>0:
                if v<=num:
                    output.append(k)
                    num -=v
                else:
                    break
        return res.join(output)