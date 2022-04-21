def generateDocument(chars, doc):
  for currentChar in doc: 
    charsFrequency = countCharFrequency(currentChar, chars)
    docFrequency = countCharFrequency(currentChar, doc)

    if charsFrequency < docFrequency:
      return False
  return True

def countCharFrequency(targetChar, inputString): 
  frequency = 0
  for char in inputString:
    if char == targetChar: 
      frequency += 1
  return frequency

def main(): 
  characters = "Bste!hetsi ogEAxpelrt x "
  document = "AlgoExpert is the Best!"
  print(generateDocument(characters, document))

if __name__ == "__main__": 
  main()