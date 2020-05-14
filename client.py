cus=[1,2,3,4,5,6,7,8,11,10]


dict=[(1,2), (3,4), (6,5), (6,7), (2,8), (7,9)]
tt=[]
count=0


for i in dict:

    if i[0] not in tt and i[1] not in tt:
        tt.append(i[0])
        tt.append(i[1])
        count+= 1
    elif i[0] in tt and i[1] not in tt:
        tt.append(i[1])
    elif i[1] in tt and i[0] not in tt:
        tt.append(i[0])
    print(i, count)

d = len(cus) - len(tt)

count = count + d

print(count)






 
def reverseWords(self, s: str) -> str:
        lst = s.split(" ")
        left, right = 0,len(lst)-1
        while left < right:
            lst[left] ,lst[right] = lst[right], lst[left]
            left+=1
            right-=1
        return " ".join([x for x in lst if x])
obj=reverseWords("the sky is blue")
print(obj)







class Solution:
    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1
            
    def reverse_each_word(self, l: list) -> None:
        n = len(l)
        start = end = 0
        
        while start < n:
            # go to the end of the word
            while end < n and l[end] != ' ':
                end += 1
            # reverse the word
            self.reverse(l, start, end - 1)
            # move to the next word
            start = end + 1
            end += 1
            
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # reverse the whole string
        self.reverse(s, 0, len(s) - 1)
        
        # reverse each word
        self.reverse_each_word(s)



  
	


class Solution(object):
    def numUniqueEmails(self, emails):
        emailAddresses = []
        for q in emails:
            local, domain = q.split('@')
            if('.' in local):
                local = local.replace('.', '')
            if('+' in local):
                local = local[0:local.index('+')]
            emailAddresses.append(local+'@'+domain)
        return len(dict.fromkeys(emailAddresses)) 
o=Solution()
# print(o.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
def func(n):
      if n % 5 == 0 and n  % 3 != 0:
          return "Power"
      elif n % 15 == 0:
          return "StarPower"  
      elif n % 3 == 0 and n%5!=0:
          return "Star"
      else:
        return n
      return func
obj=func(90)
print(obj)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currStr = ""
        maxLen = 0
        
        for start in range(len(s)):
            currStr = ""
            for index in range(start,len(s)):
                if s[index] not in currStr:
                    currStr += s[index]
                    maxLen = max(maxLen, len(currStr))
                else:
                    break
        return maxLen
obj=Solution()
print(obj.lengthOfLongestSubstring("teradata"))



def findLongestSubstring(string): 

  n = len(string) 

  # starting point of current substring. 
  st = 0

  # maximum length substring without 
  # repeating characters. 
  maxlen = 0

  # starting index of maximum 
  # length substring. 
  start = 0

  # Hash Map to store last occurrence 
  # of each already visited character. 
  pos = {} 

  # Last occurrence of first 
  # character is index 0 
  pos[string[0]] = 0

  for i in range(1, n): 

      # If this character is not present in hash, 
      # then this is first occurrence of this 
      # character, store this in hash. 
      if string[i] not in pos: 
          pos[string[i]] = i 

      else: 
          # If this character is present in hash then 
          # this character has previous occurrence, 
          # check if that occurrence is before or after 
          # starting point of current substring. 
          if pos[string[i]] >= st: 

              # find length of current substring and 
              # update maxlen and start accordingly. 
              currlen = i - st 
              if maxlen < currlen: 
                  maxlen = currlen 
                  start = st 

              # Next substring will start after the last 
              # occurrence of current character to avoid 
              # its repetition. 
              st = pos[string[i]] + 1
          
          # Update last occurrence of 
          # current character. 
          pos[string[i]] = i 
      
  # Compare length of last substring with maxlen 
  # and update maxlen and start accordingly. 
  if maxlen < i - st: 
      maxlen = i - st 
      start = st 

  return string[start : start + maxlen] 
 
obj=findLongestSubstring("teradtaa")
print(obj, len(obj))