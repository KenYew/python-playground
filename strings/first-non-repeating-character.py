# O(n) Time | O(1) Space - where n is the length of the input string
# O(1) Space because input string only has lowercase English-alphabet letters hence the hash table will never have more than 26 character frequencies.
def firstNonRepeatingCharacter(string):
    # 1: Initialise a dictionary to keep track of the frequencies of each character of the input string
    charFrequencies = {}
    # 2: Loop through each character of the input string
    for char in string:
        # 3: Create a key-value pair - where the key is the currentChar and value is the frequency of that char.
        charFrequencies[char] = charFrequencies.get(char, 0) + 1
        # 4: During traversal, if currentChar is found again in the charFrequencies dictionary, the frequency value will be incremented by 1. This keeps track of the character's frequency when iterating through the input string.
        """
        # dict.get() method: 
        # param (1): key to be searched in the dictionary
        # param (2): default value to be returned if key is not found
        """
        
    # 3: Once we have built our charFrequencies hash table, iterate through the input string again
    for idx in range(len(string)): 
        # 4: Extract the currentChar from currentIdx
        char = string[idx] 
        # 5: If currentChar has a frequency of 1 based on the hash table,
        if charFrequencies[char] == 1:
            # 6: Return the idx immediately as this will be the first non repeating (unique) character
            return idx 
    # 7: Otherwise, there are no unique characters, so return -1
    return -1