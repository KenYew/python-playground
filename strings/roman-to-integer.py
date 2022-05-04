def romanToInteger(string):
  table = {
      "I": 1, 
      "V": 5,
      "X": 10, 
      "L": 50,
      "C": 100,
      "D": 500, 
      "M": 1000
  }
  result = 0

  for idx in range(len(string)): 
    if idx + 1 < len(string) and table[string[idx]] < table[string[idx + 1]]:
      result -= table[string[idx]]
    else:
      result += table[string[idx]]

  return result

def main(): 
  string = "MCMXCIV"
  print(romanToInteger(string))

if __name__ == "__main__": 
  main()