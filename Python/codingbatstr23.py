"""Return True if the string "cat" and "dog" appear the same number of times in the given string.


cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True"""
def cat_dog(str):
  c,d=0,0
  for i in range(len(str)-2):
    if str[i:i+3]=='cat':
      c+=1
    if str[i:i+3]=='dog':
      d+=1
  if c==d:
    return True
  return False  
