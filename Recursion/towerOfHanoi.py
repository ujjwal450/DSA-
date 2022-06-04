def towerOfHanoi(n, a,b,c):
  if n == 1:
    print(f'Move 1 from {a} to {c}')
    return
  towerOfHanoi(n-1,a,c,b)
  print(f'move {n} from {a} to {c}')
  towerOfHanoi(n-1, b, a, c)

towerOfHanoi(1, 'A', 'B', 'C')

# first move n-1 disk from A to B using C as aux rod then move nth disk from A to C the move n-1 disk from B to C using A as aux
