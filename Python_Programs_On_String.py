'''
Problem 1:
Given a string, return a string where for every char in the original, there are two chars.


double_char('The') ? 'TThhee'
double_char('AAbb') ? 'AAAAbbbb'
double_char('Hi-There') ? 'HHii--TThheerree'

Solution
'''

def double_char(str):
  str1=''
  length=len(str)
  for i in range(0,length):
    str1=str1+str[i]*2
  return str1
double_char('Python')

'''
Problem 2:

Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.


end_other('Hiabc', 'abc') ? True
end_other('AbC', 'HiaBc') ? True
end_other('abc', 'abXabc') ? True

Solution:
'''
def end_other(str1,str2):
    str1=str1.lower()
    str2=str2.lower()

    if len(str1) < len(str2):
        if str2[-3:] == str1:
            print(True)
        else:
            print(False)
    elif len(str2) < len(str1):
        if str1[-3:] == str2:
            print(True)
        else:
            print(False)
    else:
        if str1 == str2:
            print(True)
        else:
            print(False)
end_other("abc","defabc")

'''
Problem 3:

Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.


xyz_there('abcxyz') ? True
xyz_there('abc.xyz') ? False
xyz_there('xyz.abc') ? True

Solution:
'''

def xyz_there(str):
 if len(str) < 3:
   return False
 for i in range(0,len(str)-1):
  if str[i]=='x' and str[i+1]=='y' and str[i+2]=='z':
    return True
  elif str[i]=='.'and str[i+1]=='x' and str[i+2]=='y' and str[i+3]=='z':
    continue
  return False

'''
Problem 4:


Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.


count_code('aaacodebbb') ? 1
count_code('codexxcode') ? 2
count_code('cozexxcope') ? 2

Solution:
'''
def count_code(str):
  count=0
  for i in range(0,len(str)-3):
    if str[i]=='c' and str[i+1]=='o' and str[i+3]=='e':
      count=count+1
  return count

'''
Problem 5:


Given a string, return a string where for every char in the original, there are two chars.


double_char('The') ? 'TThhee'
double_char('AAbb') ? 'AAAAbbbb'
double_char('Hi-There') ? 'HHii--TThheerree'

Solution:

'''
def double_char(str):
  str1=''
  length=len(str)
  for i in range(0,length):
    str1=str1+str[i]*2
  return str1

'''
Problem 6:


Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.


without_end('Hello') ? 'ell'
without_end('java') ? 'av'
without_end('coding') ? 'odin'

Solution:
'''
def without_end(str):
  return str[1:len(str)-1]

'''
Problem 7:

Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.


left2('Hello') ? 'lloHe'
left2('java') ? 'vaja'
left2('Hi') ? 'Hi'

Solution:
'''

def left2(str):
  return str[2:]+str[0:2]

'''

Problem 8:


Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.


extra_end('Hello') ? 'lololo'
extra_end('ab') ? 'ababab'
extra_end('Hi') ? 'HiHiHi'

Solution:
'''
def extra_end(str):
  return str[len(str)-2:]*3

'''
Problem 9:


Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".


first_half('WooHoo') ? 'Woo'
first_half('HelloThere') ? 'Hello'
first_half('abcdef') ? 'abc'

Solution:
'''
def first_half(str):
  return str[:len(str)/2]
