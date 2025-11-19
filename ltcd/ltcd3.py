# My Solution for the leetcode problem 9. Palindrome Number

class Solution:
    def isPalindrome(self,x):
        self.x = x
        mylist = []
        flag = ""
        for i in str(x):
            mylist.append(i)
        while len(mylist) > 0:
            i = 0
            j = len(mylist)-1
            if mylist[i] == mylist[j]:
                if len(mylist) > 1:
                    mylist.pop(j)
                    mylist.pop(i)
                    if len(mylist) == 0:
                        flag = "true"
                else:
                    flag = "true"
                    break
            else:
                flag = "false"
                break
        if flag == "true":
            return True
        else:
            return False

a = Solution()
print(a.isPalindrome(11))