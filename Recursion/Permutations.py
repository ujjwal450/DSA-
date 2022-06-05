def permutations(s, i = 0):
  if i == len(s)-1:
    print(s)
    return
  for j in range(i, len(s)):
    s[i], s[j] = s[j],s[i]
    permutations(s, i+1)
    s[i], s[j] = s[j],s[i]
  
  
permutations(['A','B','C'], 0)