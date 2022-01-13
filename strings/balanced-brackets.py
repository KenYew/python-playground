def balancedBrackets(string):
    # 1: Initialise a mapping of parentheses (where left brackets are keys and right brackets are values)
    dict = {'(':')', '{':'}','[':']'}
    stack = []
    
    # 2: Loop through every character of the input string
    for char in string:
        # 3: If the character is a left bracket (, {, [, it is a valid key in dict, so we append it to the stack
        if char in dict: 
            stack.append(char)
        # 4: Else if it's a right bracket ), }, ], check if stack is empty or check if the brackets are matching 
        elif len(stack) == 0 or dict[stack.pop()] != char: 
            return False
    # 5: Finally, check if the stack still contains any unmatched left bracket
    return len(stack) == 0

# O(n) Time | O(n) Space
def balancedBrackets(string):
    openingBrackets = "([{"
    closingBrackets = ")]}"
    matchingBrackets = {")": "(", "]": "[", "}": "{"}
    stack = []
    
    for char in string: 
        if char in openingBrackets:
            stack.append(char)
        elif char in closingBrackets: 
            if len(stack) == 0:
                return False
            if stack[-1] == matchingBrackets[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

string = "()[]{}"
print(balancedBrackets(string))