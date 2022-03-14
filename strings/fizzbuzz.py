# O(n) Time | O(n) Space
def fizzBuzz(n):
    result = []
    for idx in range(1, n + 1): 
        string = ""
        if idx % 3 == 0:
            string += "Fizz"
        if idx % 5 == 0: 
            string += "Buzz"
        result.append(str(idx) if not len(string) else string)
    return result