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
    else:
      oneDigitWord = f' {oneDigit[inputNumber % 10]}' if inputNumber % 10 else ""
      return f'{tens[inputNumber // 10]}{oneDigitWord}'

  def getThreeDigitNumber(inputNumber):
    if not inputNumber:
      return ""
    elif not inputNumber // 100: 
      return getTwoDigitNumber(inputNumber)
    else: 
      twoDigitWord = f' {getTwoDigitNumber(inputNumber % 100)}' if inputNumber % 100 else ""
      return f'{oneDigit[inputNumber // 100]} Hundred{twoDigitWord}'
  
  if inputNumber < 0 or inputNumber > 2 ** 31 - 1:
    return "Invalid Input!"

  if inputNumber == 0:
    return "Zero"

  billions = inputNumber // 1000000000 
  millions = (inputNumber % 1000000000) // 1000000 
  thousands = (inputNumber % 1000000) // 1000
  lastThreeDigits = inputNumber % 1000 

  result = []
  if billions: 
    result.append(f'{getThreeDigitNumber(billions)} Billion')
  if millions: 
    result.append(f'{getThreeDigitNumber(millions)} Million')
  if thousands: 
    result.append(f'{getThreeDigitNumber(thousands)} Thousand')
  if lastThreeDigits: 
    result.append(getThreeDigitNumber(lastThreeDigits))
  return " ".join(result).rstrip()

def main():
  # inputNumber = 1234567890
  inputNumber = 2147483647
  # inputNumber = 1234500000
  print(integerToWords(inputNumber))

if __name__ == "__main__":
  main()