
def recur(k):
    if k>0:
        return k+recur(k-1)
    else:
        return 0
print("\n\nRecursion Example Results")
print(recur(6))

"""
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

"""
