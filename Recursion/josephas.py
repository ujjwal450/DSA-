
def josephas(n,k):
  if (n == 1):
    return 1
  else:
    return (josephas(n-1,k)+k-1)%n+1
    
print(josephas(14,2))