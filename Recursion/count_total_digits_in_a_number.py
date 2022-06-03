def count_total_digit(n):
  if n//10 != 0:
    return 1+ count_total_digit(n//10)
  elif n>=0:
    return 1
  else:
    return 0
  
print(count_total_digit(123))