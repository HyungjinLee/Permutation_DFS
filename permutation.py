def permutation(arr, r) :
  used = [0] * len(arr)
  stack = [[[],used]] # chosen elements, used
  
  while stack :
      cur = stack.pop()
      if len(cur[0]) == r :
          print(' '.join(map(str,cur[0])))
          continue
        
      for i in range (len(arr)) :
          if not cur[1][i] :
              stack.append((cur[0] + [arr[i]], [1 if j==i else cur[1][j] for j in range (len(cur[1]))])) # reinitialization

print(permutation([1,2,3,4,5],5))