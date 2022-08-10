# 中心点枚举算法
class Solution:
    def longest_palindrome(self, s):
        if not s:
            return ""
            
        answer = (0, 0)
        for mid in range(len(s)):
            answer = max(answer, self.get_palindrom_from(s, mid, mid))
            print(answer)
            answer = max(answer, self.get_palindrom_from(s, mid, mid + 1))
            print(answer)
            print(s[answer[1]: answer[0] + answer[1]] )

        return s[answer[1]: answer[0] + answer[1]]    
        
    def get_palindrom_from(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            print(left)
            right += 1
            print(right)

            print(right - left - 1, left + 1)
        return (right - left - 1, left + 1)

find = Solution()
substr = find.longest_palindrome("huohuohwwnwwh")
print(substr)