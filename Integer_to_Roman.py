class Solution(object):
    def intToRoman(self, s):
      lis=[]
      while s>0:
        if s>=1000:
          lis.append('M')
          s-=1000
        elif s>=900:
          lis.append('C'+'M')
          s-=900
        elif s>=500:
          lis.append('D')
          s-=500
        elif s>=400:
          lis.append('C'+'D')
          s-=400
        elif s>=100:
          lis.append('C')
          s-=100
        elif s>=90:
          lis.append('X'+'C')
          s-=90
        elif s>=50:
          lis.append('L')
          s-=50
        elif s>=40:
          lis.append('X' +'L') 
          s-=40
        elif s>=9:
          lis.append((10-s) *'I' +'X')
          s-=10
        elif s>5:
          lis.append('V' + (s-5)*'I')
          s=0
          # print(s)
        elif s>3 & s<=5:
          lis.append((5-s)*'I' + 'V')
          s=0
        elif s<=3:
          lis.append("I" * s)
          s=0
      str1 = ""
      return (str1.join(lis))
sol=Solution()
sol.intToRoman(58)
