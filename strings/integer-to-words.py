# O(1) Time | O(1) Space
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

  def getTwoDigits(inputNumber): 
    if not inputNumber:
      return ""
    elif inputNumber < 10:
      return oneDigit[inputNumber]
    elif inputNumber < 20: 
      return twoDigits[inputNumber]
    else: # 20 < inputNumber < 99
      tensDigit = inputNumber // 10
      onesDigit = inputNumber % 10 
      if onesDigit: 
        return f'{tens[tensDigit]} {oneDigit[onesDigit]}'
      else:
        return f'{tens[tensDigit]}'

  def getThreeDigits(inputNumber): # 100 < inputNumber < 999
    if not inputNumber:
      return ""
    elif not inputNumber // 100: 
      return getTwoDigits(inputNumber)
    else:
      hundredsDigit = inputNumber // 100
      lastTwoDigits = inputNumber % 100
      if lastTwoDigits: 
        return f'{oneDigit[hundredsDigit]} Hundred {getTwoDigits(lastTwoDigits)}'
      else:
        return f'{oneDigit[hundredsDigit]} Hundred'

  if inputNumber == 0: 
    return "Zero"

  MAX_INT = 2 ** 31 - 1
  if inputNumber < 0 or inputNumber > MAX_INT: 
    return "Invalid Input!"
  
  billions = inputNumber // 1000000000 # 1,000,000,000 - 2,147,483,647
  millions = (inputNumber % 1000000000) // 1000000 # 1,000,000 - 999,999,999
  thousands = (inputNumber % 1000000)  // 1000 # 1,000 - 999,999
  lastThreeDigits = inputNumber % 1000
  
  result = []
  if billions: 
    result.append(f'{oneDigit[billions]} Billion')
  if millions:
    result.append(f'{getThreeDigits(millions)} Million')
  if thousands:
    result.append(f'{getThreeDigits(thousands)} Thousand')
  if lastThreeDigits:
    result.append(f'{getThreeDigits(lastThreeDigits)}')
  return " ".join(result)

  ## If problem constraints are 0 < inputNumber < 999
  # if inputNumber < 100:
  #   return getTwoDigits(inputNumber)
  # else:
  #   return getThreeDigits(inputNumber)

def main(): 
  t1 = 11
  t2 = 1001017090
  t3 = 2147483647
  t4 = 0
  t5 = 3000000000
  t6 = -1
  
  print(integerToWords(t1))
  print(integerToWords(t2))
  print(integerToWords(t3))
  print(integerToWords(t4))
  print(integerToWords(t5))
  print(integerToWords(t6))

if __name__ == "__main__":
  main()
  
# def integerToWords(inputNumber): 
#   oneDigit = {
#     1: 'One',
#     2: 'Two',
#     3: 'Three',
#     4: 'Four',
#     5: 'Five',
#     6: 'Six',
#     7: 'Seven',
#     8: 'Eight',
#     9: 'Nine'
#   }

#   twoDigits = {
#     10: 'Ten',
#     11: 'Eleven',
#     12: 'Twelve',
#     13: 'Thirteen',
#     14: 'Fourteen',
#     15: 'Fifteen',
#     16: 'Sixteen',
#     17: 'Seventeen',
#     18: 'Eighteen',
#     19: 'Nineteen'
#   }

#   tens = {
#     2: 'Twenty',
#     3: 'Thirty',
#     4: 'Forty',
#     5: 'Fifty',
#     6: 'Sixty',
#     7: 'Seventy',
#     8: 'Eighty',
#     9: 'Ninety'
#   }

#   def getTwoDigitNumber(inputNumber): 
#     if not inputNumber:
#       return ""
#     elif inputNumber < 10: 
#       return oneDigit[inputNumber]
#     elif inputNumber < 20: 
#       return twoDigits[inputNumber]
#     else:
#       oneDigitWord = f' {oneDigit[inputNumber % 10]}' if inputNumber % 10 else ""
#       return f'{tens[inputNumber // 10]}{oneDigitWord}'

#   def getThreeDigitNumber(inputNumber):
#     if not inputNumber:
#       return ""
#     elif not inputNumber // 100: 
#       return getTwoDigitNumber(inputNumber)
#     else: 
#       twoDigitWord = f' {getTwoDigitNumber(inputNumber % 100)}' if inputNumber % 100 else ""
#       return f'{oneDigit[inputNumber // 100]} Hundred{twoDigitWord}'
  
#   if inputNumber < 0 or inputNumber > 2 ** 31 - 1:
#     return "Invalid Input!"

#   if inputNumber == 0:
#     return "Zero"

#   billions = inputNumber // 1000000000 
#   millions = (inputNumber % 1000000000) // 1000000 
#   thousands = (inputNumber % 1000000) // 1000
#   lastThreeDigits = inputNumber % 1000 

#   result = []
#   if billions: 
#     result.append(f'{getThreeDigitNumber(billions)} Billion')
#   if millions: 
#     result.append(f'{getThreeDigitNumber(millions)} Million')
#   if thousands: 
#     result.append(f'{getThreeDigitNumber(thousands)} Thousand')
#   if lastThreeDigits: 
#     result.append(getThreeDigitNumber(lastThreeDigits))
#   return " ".join(result).rstrip()

# def main():
#   # inputNumber = 1234567890
#   inputNumber = 2147483647
#   # inputNumber = 1234500000
#   print(integerToWords(inputNumber))

# if __name__ == "__main__":
#   main()