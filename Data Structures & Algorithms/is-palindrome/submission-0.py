class Solution:
    def isPalindrome(self, s: str) -> bool:
        check="".join(filter(str.isalnum,s.upper()))
        start=0
        end=-1
        for _ in range(len(check)):
            if check[start]!=check[end]:
                return False
                break
            start+=1
            end-=1
        else:
            return True