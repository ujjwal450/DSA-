def ropeCuttingProblem(n, a,b,c):
  if n == 0:
    return 0
  if n<0:
    return -1
  res = max(
  ropeCuttingProblem(n-a, a,b,c),
  ropeCuttingProblem(n-b, a,b,c),
  ropeCuttingProblem(n-c, a,b,c)
  )
  if res == -1:
    return -1
  return res+1

print(ropeCuttingProblem(5, 3,2,1))