# O(1) Time because the patterns to match have constant length
# O(1) Space
import re
def validateIPAddress(IP): 
  chunkIPv4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
  patternIPv4 = re.compile(r'^(' + chunkIPv4 + r'\.){3}' + chunkIPv4 + r'$')
  
  chunkIPv6 = r'([0-9a-fA-F]{1,4})'
  patternIPv6 = re.compile(r'^(' + chunkIPv6 + r'\:){7}' + chunkIPv6 + r'$')
    
  if patternIPv4.match(IP):
      return "IPv4"
  return "IPv6" if patternIPv6.match(IP) else "Neither"

def main(): 
  IP = "172.16.254.1" # IPv4
  IP = "2001:0db8:85a3:0:0:8A2E:0370:7334" # IPv6
  IP = "256.256.256.256" # Neither
  print(validateIPAddress(IP))

if __name__ == "__main__":
  main()