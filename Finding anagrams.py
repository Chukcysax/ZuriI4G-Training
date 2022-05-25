# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True
from collections import Counter


def find_anagrams(data1, data2):
    return Counter (data1) == Counter (data2)

        
 #main function
if __name__ == "__main__" :
    data1 = 'elvis'
    data2 = 'lives'
    print (find_anagrams (data1, data2)) 


