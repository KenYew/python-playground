# O(1) Time | O(1) Space
# Time Complexity: Since an IP address is a 32 bit integer (e.g.: 0-255.0-255.0-255.0-255), you will only need to compute at most at a constant 2^32 numbers hence O(2^32) which can be reduced to O(1). The size of the input, n is independent and 2^32 is the absolute constant upper bound.
# Space Complexity: Since you can only generate a list that is at most 2^32 IP addresses in it (2^32 being the absolute constant upper bound), the space complexity is O(2^32) which can be reduced to O(1).

def validIPAddresses(string):
    ipAddressesFound = []
    # [192 . 1 . 68 . 0]
    # [    i   j    k  ] # i, j, k pointers represent the dots in the IP adddresses
    
    # For the 1st octet, you can only place the dot at positions 1 - 3. The pointer i gives a range to slice the string for the first IP octet.
    for i in range(1, min(len(string), 4)): # We start at range 1 so that we will never have an empty string
        currentIPAddressParts = ['', '', '', ''] 
        currentIPAddressParts[0] = string[:i] # slice the input string until pointer i for the 1st IP octet
        if not isValidPart(currentIPAddressParts[0]): # then check of this sliced string is a valid IP (0-255) with not leading zeroes (e.g.: 01)
            continue # skip if 1st IP octet is invalid
        
        # For thhe 2nd octet, we select a range (for j) after pointer i and spanning at most 3 digits (to honour the valid IP range of 0-255)
        for j in range(i + 1, i + min(len(string) - i, 4)): 
            currentIPAddressParts[1] = string[i:j] # slice the input string starting from index i to j for 2nd IP octet
            if not isValidPart(currentIPAddressParts[1]):
                continue # skip if 2nd IP octet is invalid
            
            # For the 3rd octet, we select a range (for k) after pointer j and spanning at most 3 digits (to honour the valid IP range of 0-255)
            for k in range(j + 1, j + min(len(string) - j, 4)):
                currentIPAddressParts[2] = string[j:k] # slice the input string starting from index j to k for 3rd IP octet
                currentIPAddressParts[3] = string[k:] # slice the rest of the input string starting index k onwards for 4th IP octet
                # if 3rd and 4th IP octets are valid, then we found the right combinations of IP dot pointers that make a valid IP address,
                if isValidPart(currentIPAddressParts[2]) and isValidPart(currentIPAddressParts[3]):
                    ipAddressesFound.append('.'.join(currentIPAddressParts)) # Add the answer and delimiting all IP address octets with '.'
    
    return ipAddressesFound
        
def isValidPart(string):
    stringAsInt = int(string) # Converting str to int helps remove any leading zeroes in string (e.g.: 00 -> 0 and 01 -> 1)
    if stringAsInt > 255: 
        return False
    return len(string) == len(str(stringAsInt)) # Checks if there are any leading 0's

# SOLUTION: THREE POINTERS: Set 3 pointers i, j, k for each IP dots, create 3 FOR loops each to slice string into 4 possible IP octets and check if the octets are valid (0-255), if all 4 octets are valid, then join the valid octets with '.' and append to answers array.

string = "1921680"
print(validIPAddresses(string))