# Range 1-999
wordDictionary = {
  0: "",
  1: "One",
  2: "Two",
  3: "Three",
  4: "Four",
  5: "Five",
  6: "Six",
  7: "Seven",
  8: "Eight",
  9: "Nine",
  10: "Ten",
  11: "Eleven",
  12: "Twelve",
  13: "Thirteen",
  14: "Fourteen",
  15: "Fifteen",
  16: "Sixteen",
  17: "Seventeen",
  18: "Eighteen",
  19: "Nineteen",
  20: "Twenty",
  30: "Thirty",
  40: "Forty",
  50: "Fifty",
  60: "Sixty",
  70: "Seventy",
  80: "Eighty",
  90: "Ninety",
  100: "Hundred",
}

def integerToWords(inputNumber):
  result = [] 
  if not inputNumber or inputNumber < 0 or inputNumber > 999: 
    return "Invalid Input!"
  
  if inputNumber < 20: 
    return wordDictionary[inputNumber]

  hundredsPosition = inputNumber // 100
  tensPosition = (inputNumber % 100) // 10
  onesPosition = inputNumber % 10

  if hundredsPosition > 0: 
    result.append(f'{wordDictionary[hundredsPosition]} {wordDictionary[100]}')

  if tensPosition >= 2: 
    result.append(wordDictionary[10 * tensPosition])
    if onesPosition > 0: 
      result.append(wordDictionary[onesPosition])
  else:
    result.append(wordDictionary[inputNumber - hundredsPosition * 100])

  return " ".join(result) 

def main():
  inputNumber = 999
  print(integerToWords(inputNumber))

if __name__ == "__main__":
  main()

# Range 1-2^31-1
def integerToWords(inputNumber): 
  oneDigit = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine'
  }

  twoDigits = {
    10: 'Ten',
    11: 'Eleven',
    12: 'Twelve',
    13: 'Thirteen',
    14: 'Fourteen',
    15: 'Fifteen',
    16: 'Sixteen',
    17: 'Seventeen',
    18: 'Eighteen',
    19: 'Nineteen'
  }

  tens = {
    2: 'Twenty',
    3: 'Thirty',
    4: 'Forty',
    5: 'Fifty',
    6: 'Sixty',
    7: 'Seventy',
    8: 'Eighty',
    9: 'Ninety'
  }

  def getTwoDigitNumber(inputNumber): 
    if not inputNumber:
      return ""
    elif inputNumber < 10: 
      return oneDigit[inputNumber]
    elif inputNumber < 20: 
      return twoDigits[inputNumber]

    oneDigitWord = f' {oneDigit[inputNumber % 10]}' if inputNumber % 10 else ""
    return f'{tens[inputNumber // 10]}{oneDigitWord}'

  def getThreeDigitNumber(inputNumber):
    if not inputNumber:
      return ""
    if not inputNumber // 100: 
      return getTwoDigitNumber(inputNumber)

    twoDigitWord = f' {getTwoDigitNumber(inputNumber % 100)}' if inputNumber % 100 else ""
    return f'{oneDigit[inputNumber // 100]} Hundred{twoDigitWord}'

  
  if not inputNumber or inputNumber < 0 or inputNumber > 2 ** 31 - 1:
    return "Invalid Input!"

  if inputNumber == 0:
    return "Zero"

  billions = inputNumber // 1000000000 
  millions = (inputNumber % 1000000000) // 1000000 
  thousands = (inputNumber % 1000000) // 1000
  lastThreeDigits = inputNumber % 1000 

  result = []
  if billions: 
    result.append(f'{getThreeDigitNumber(billions)} Billion ')
  if millions: 
    result.append(f'{getThreeDigitNumber(millions)} Million ')
  if thousands: 
    result.append(f'{getThreeDigitNumber(thousands)} Thousand ')
  if lastThreeDigits: 
    result.append(getThreeDigitNumber(lastThreeDigits))
  return "".join(result).rstrip()

def main():
  # inputNumber = 1234567890
  # inputNumber = 2147483647
  inputNumber = 1234500000
  print(integerToWords(inputNumber))

if __name__ == "__main__":
  main()