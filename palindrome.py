#Given an integer x, return true if x is a palindrome , and false otherwise.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        #optimized
        if x < 0:
            return False
        for i in range(int(x/2)):


        # bruteforce
        # xstr = str(x)
        # for i in range((len(xstr) // 2)):
        #     if xstr[i] != xstr[-(i+1)]:
        #         return(False)
        # return(True)

if __name__ == "__main__":

    result = Solution().isPalindrome(12321)
    print(result)
