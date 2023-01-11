class Solution(object):
    def get_nums(self,p):
      pp={}
      ch=[]
      main_p=[]
      i=0
      for pi in p:
        if pi not in ch:
          i+=1
          ch.append(pi)
          pp[pi]=i
          main_p.append(i)
        else:
            for chr,num in pp.items():
              # print(chr,num)
              if pi==chr:
                pp[pi]=num
                main_p.append(num)
      return main_p

    def wordPattern(self, pattern, s):
          p=list(pattern)
          p_nums=self.get_nums(p)
          q=s.split()
          q_nums=self.get_nums(q)
          if p_nums==q_nums:
            return True
          else:
            return False
sol=Solution()
sol.wordPattern('abba', 'dog cat cat dog')
