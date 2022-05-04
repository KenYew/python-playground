def integerToRoman(num):
  table = {
      1000: "M",
      900: "CM",
      500: "D",
      400: "CD",
      100: "C",
      90: "XC",
      50: "L",
      40: "XL",
      10: "X",
      9: "IX",
      5: "V",
      4: "IV",
      1: "I"
  }
  result = ""
  for key in table: 
    if num <= 0:
      break
    result += (num // key) * table[key]
    num %= key
  return result

def main(): 
  num = 1994
  print(integerToRoman(num))

if __name__ == "__main__":
  main()