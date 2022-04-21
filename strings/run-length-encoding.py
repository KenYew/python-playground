def runLengthEncoding(string): 
  encodedString = []
  currentLength = 0
  for idx in range(1, len(string)): 
    currentChar = string[idx]
    previousChar = string[idx - 1]

    if currentChar != previousChar or currentLength == 9: 
      encodedString.append(str(currentLength))
      encodedString.append(previousChar)
      currentLength = 0

    currentLength += 1
  
  encodedString.append(str(currentLength))
  encodedString.append(string[len(string) - 1])

  return "".join(encodedString)

def main():
  string = "AAAAAAAAAAAAABBCCCCDD"
  print(runLengthEncoding(string))

if __name__ == "__main__": 
  main()