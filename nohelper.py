def isEven(a): # this is the helper function
  return a % 2 == 0

def processNumber(b):
  if isEven(b):
    print("even number")
  else:
    print("odd number")
