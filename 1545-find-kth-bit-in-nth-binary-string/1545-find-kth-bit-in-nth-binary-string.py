class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # sequence = "0"

        # # Generate sequence until we have enough elements or reach nth iteration
        # for i in range(1, n):
        #     if k <= len(sequence):
        #         break
        #     sequence += "1"

        #     # Append the inverted and reversed part of the existing sequence
        #     inverted = "".join(
        #         "1" if bit == "0" else "0" for bit in sequence[:-1]
        #     )
        #     sequence += inverted[::-1]

        # # Return the kth bit
        # return sequence[k - 1]

        # Find the position of the rightmost set bit in k
        # This helps determine which "section" of the string we're in
        position_in_section = k & -k

        # Determine if k is in the inverted part of the string
        # This checks if the bit to the left of the rightmost set bit is 1
        is_in_inverted_part = ((k // position_in_section) >> 1 & 1) == 1

        # Determine if the original bit (before any inversion) would be 1
        # This is true if k is even (i.e., its least significant bit is 0)
        original_bit_is_one = (k & 1) == 0

        if is_in_inverted_part:
            # If we're in the inverted part, we need to flip the bit
            return "0" if original_bit_is_one else "1"
        else:
            # If we're not in the inverted part, return the original bit
            return "1" if original_bit_is_one else "0"