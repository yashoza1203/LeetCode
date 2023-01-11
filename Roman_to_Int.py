class Solution(object):
  def romanToInt(self, roman_no):
    Sum=0
    LL={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    combination=['IV','IX','CM','CD','XC','XL']
    for i in combination:
      if i in roman_no:
        list_r=list(i)
        num=LL[list_r[1]]-LL[list_r[0]]
        Sum+=num
        roman_no=roman_no.replace(i,'')
    list_rom=list(roman_no)

    for i in list_rom:
      Sum+=LL[i]
      roman_no=roman_no.replace(i,'')
    return Sum

sol=Solution()
sol.romanToInt('MCDLXXVI')
