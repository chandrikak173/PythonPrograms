'''
Problem1:
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.


sleep_in(False, False) ? True
sleep_in(True, False) ? False
sleep_in(False, True) ? True

Solution:
'''
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False
print(sleep_in(False, False))

'''
Given a string, return a new string where the first and last chars have been exchanged.


front_back('code') ? 'eodc'
front_back('a') ? 'a'
front_back('ab') ? 'ba'

Solution:
'''
def front_back(str):
  if len(str) <= 1:
    return str
  else:
   length=len(str)
   str1=str[length-1]+str[1:length-1]+str[0]
   return str1
print(front_back('code'))


'''
Problem 3:

Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).


missing_char('kitten', 1) ? 'ktten'
missing_char('kitten', 0) ? 'itten'
missing_char('kitten', 4) ? 'kittn'

Solution:
'''
def missing_char(str, n):
  string1=str[0:n]+str[n+1:]
  return string1
print(missing_char('kitten', 4))
'''
Problem 4:
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;


front_times('Chocolate', 2) ? 'ChoCho'
front_times('Chocolate', 3) ? 'ChoChoCho'
front_times('Abc', 3) ? 'AbcAbcAbc'

Solution:
'''
def front_times(str, n):
  if len(str) <= 3:
    return str*n
  else:
    return str[0:3]*n
print(front_times('Chocolate', 2))

'''
Problem 5:

Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".


string_bits('Hello') ? 'Hlo'
string_bits('Hi') ? 'H'
string_bits('Heeololeo') ? 'Hello'

Solution:
'''
def string_bits(str):
  return str[::2]
print(string_bits('Heeololeo'))

'''
Problem 6:
Given an array of ints, return the number of 9's in the array.


array_count9([1, 2, 9]) ? 1
array_count9([1, 9, 9]) ? 2
array_count9([1, 9, 9, 3, 9]) ? 3

Solution:
'''
def array_count9(nums):
  j=0
  for i in range(len(nums)):
    if nums[i]==9:
      j=j+1
  return j
print(array_count9([1, 9, 9, 3, 9]))

'''
Problem 7:

Given a non-empty string like "Code" return a string like "CCoCodCode".


string_splosion('Code') ? 'CCoCodCode'
string_splosion('abc') ? 'aababc'
string_splosion('ab') ? 'aab'

Solution:
'''
def string_splosion(str):
  result = ""
  # On each iteration, add the substring of the chars 0..i
  for i in range(len(str)):
    result = result + str[:i+1]
  return result
print(string_splosion('Code'))

'''
Problem 8:
Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.


array_front9([1, 2, 9, 3, 4]) ? True
array_front9([1, 2, 3, 4, 9]) ? False
array_front9([1, 2, 3, 4, 5]) ? False

Solution:
'''
def array_front9(nums):
  # First figure the end for the loop
  end = len(nums)
  if end > 4:
    end = 4
  
  for i in range(end):  # loop over index [0, 1, 2, 3]
    if nums[i] == 9:
      return True
  return False
print(array_front9([1, 2, 3, 4, 5]))

'''
Problem 9:

Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

array123([1, 1, 2, 3, 1]) ? True
array123([1, 1, 2, 4, 1]) ? False
array123([1, 1, 2, 1, 2, 3]) ? True

Solution:
'''
def array123(nums):
  for i in range(len(nums)-2):
   if nums[i]== 1 and nums[i+1]==2 and nums[i+2]==3:
     return True
  return False
print(array123([1, 1, 2, 1, 2, 3]))

'''
Problem 10:

Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.


string_match('xxcaazz', 'xxbaaz') ? 3
string_match('abc', 'abc') ? 2
string_match('abc', 'axc') ? 0

Solution:
'''
def string_match(a, b):
  num=0
  if len(a) < len(b):
    for i in range(len(a)-1):
      if a[i] == b[i] and a[i+1]==b[i+1]:
        num=num+1
  else:
    for i in range(len(b)-1):
      if a[i] == b[i] and a[i+1]==b[i+1]:
        num=num+1
    
  return num
print(string_match('abc', 'axc'))