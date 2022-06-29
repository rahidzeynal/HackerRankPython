if __name__ == '__main__':
  marksheet = []
  ls = []
  for _ in range(0,int(input())):
    name = input()
    score = float(input())
    ls.append(score)
    marksheet.append([score, name])
  marksheet.sort()
  
  mn = min(ls)
  #print(mn)
  #print(len(name))
  for i in range(len(ls)-1):
    if marksheet[i][0] == mn:
      marksheet.remove(marksheet[i])
    if ls[i] == mn:
      ls.remove(ls[i])
  #print(marksheet)
  
  ms = []
  mn1 = min(ls)
  #print(len(ls))
  for i in range(len(ls)):
    if marksheet[i][0] == mn1:
      #print(marksheet[i][0])
      score = marksheet[i][0]
      name = marksheet[i][1]
      ms.append([name, score])
  #print(len(ms))
  ms.sort()
  
  if len(ms) == 1:
    print(ms[0][0])
  else:
    for i in range(0, len(ms)):
      print(ms[i][0])
