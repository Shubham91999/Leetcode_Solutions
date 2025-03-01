class Solution:
    def reorganizeString(self, s: str) -> str:
        # Calculate the length of the string
        string_length = len(s)
      
        # Count the frequency of each character in the string
        char_count = Counter(s)
      
        # Find the maximum frequency of any character
        max_freq = max(char_count.values())
      
        # If the max frequency is more than half of the string length, round up,
        # then the task is impossible as that character would need to be adjacent to itself.
        if max_freq > (string_length + 1) // 2:
            return ''
      
        # Initialize index for placing characters
        index = 0
      
        # Create a list to store the reorganized string
        reorganized = [None] * string_length
      
        # Fill in the characters, starting with the most common
        for char, freq in char_count.most_common():
            while freq:
                # Place the character at the current index
                reorganized[index] = char
                # Decrease the frequency count
                freq -= 1
                # Move to the next even index or the first odd index if the end is reached
                index += 2
                if index >= string_length:
                    index = 1
      
        # Return the list as a string
        return ''.join(reorganized)