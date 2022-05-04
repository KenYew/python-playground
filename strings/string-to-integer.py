# O(n) Time - we visit each character in the input at most once and for each character we spend a constant amount of time.
# O(1) Space - we have used only constant space to store the sign and the result.
def stringToInteger(string: str) -> int:
    sign, idx, result = 1, 0, 0

    MAX_INT = 2 ** 31 - 1 
    MIN_INT = -2 ** 31
    
    while idx < len(string) and string[idx] == ' ':
        idx += 1
    
    if idx < len(string) and string[idx] == '+':
        sign = 1
        idx += 1
    elif idx < len(string) and string[idx] == '-':
        sign = -1
        idx += 1
    
    while idx < len(string) and string[idx].isdigit():
        digit = int(string[idx]) 
        result = 10 * result + digit 
        idx += 1

    result = sign * result 
    if result < 0: 
      return max(result, MIN_INT)
    return min(result, MAX_INT)

def main():
  string = "42"
  print(stringToInteger(string))
  print(type(stringToInteger(string)))

if __name__ == "__main__": 
  main()