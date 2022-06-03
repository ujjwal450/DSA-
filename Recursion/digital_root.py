def sumDigits(n):
    if n == 0:
      return 0
    return n%10 + sumDigits(n//10)
def digitalRoot(n):
  if n<10:
    return n
  return digitalRoot(sumDigits(n))
   
print(digitalRoot(178))
# if sum of digits is not a single digit number we call sum of digit again on that number
