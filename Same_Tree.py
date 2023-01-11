class Solution(object):
    def isSameTree(self, p, q):
      correct=0
      p=list(str(p))
      q=list(str(q))
      for pi,qi in zip(p,q):
        if pi==qi:
          correct+=1
        else:
          return False
      if correct==len(p):
        return True
      else:
        return False

sol=Solution()
sol.isSameTree([1,2,3],[1,2,3])
