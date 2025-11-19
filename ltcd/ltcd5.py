"""
My solution for the leetcode problem 13. Roman to Integer
"""

class Solution:
    def isRoman(self,s):
        mydict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        self.s = s
        r = reversed(s)
        s_rev = ''.join(r)
        mylist = list(s_rev)
        print(mylist)
        for i in range(0,len(mylist)):
            mylist[i] = mydict[mylist[i]]
        count = mylist[0]
        print(count)
        i = 0
        while i <= len(mylist)-2:
            if mylist[i] <= mylist[i+1]:
                count = count + mylist[i+1]
            else:
                count = count - mylist[i+1]
            print(count)
            i += 1
            
        return count
    
a = Solution()
print(a.isRoman("DCXXI"))
    
    






