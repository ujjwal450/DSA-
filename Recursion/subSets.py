def subSets(str, i, cur):
  if (i == len(str)):
    print(cur)
    return
  subSets(str, i+1, cur+str[i])
  subSets(str, i+1, cur)

subSets('abc', 0, '')