def reverseWordsInString(string):
  result = []
  start = 0
  # split() method implementation
  for idx, currentChar in enumerate(string): 
    if currentChar == " ": 
      result.append(string[start:idx])
      start = idx
    elif string[start] == " ": 
      result.append(" ")
      start = idx
  result.append(string[start:])
  
  # reverse() method implementation
  reverseList(result)
  return "".join(result)

def reverseList(_list): 
  left, right = 0, len(_list) - 1
  while left < right: 
    _list[left], _list[right] = _list[right], _list[left]
    left += 1
    right -= 1

string = "AlgoExpert is the best!"
print(reverseWordsInString(string))

print()