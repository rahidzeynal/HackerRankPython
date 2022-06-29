if __name__ == '__main__':
  n = int(input())
  arr = input().split()
  l = []
  for i in arr:
    if int(i) not in l:
      l.append(int(i))
    else:
      pass
  l.remove(max(l))
  print(max(l))
