if __name__ == '__main__':
    l = []
    ll = []
    a = 0
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    for key, value in student_marks.items():
      if query_name == key:
        l = value
        a = len(l)
        
        if a > 1:
          print("{:.2f}".format(sum(l)/a))
        else:
          pass
