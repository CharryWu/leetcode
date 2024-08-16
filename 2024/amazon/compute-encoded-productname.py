from collections import Counter

def computeEncodedProductName(nameString):
    # Step 1: Count frequency of each character
    char_count = Counter(nameString)

    # Step 2: Determine the first half of the palindrome
    first_half = []
    middle_char = ''

    for char in sorted(char_count.keys()):
        count = char_count[char]

        # If the character count is odd, save one occurrence for the middle
        if count % 2 != 0:
            if middle_char:
                # If there's already a middle character, it's not possible to form a palindrome
                return ""
            middle_char = char

        # Add half of the characters to the first half
        first_half.append(char * (count // 2))

    # Step 3: Form the palindrome
    first_half = ''.join(first_half)
    second_half = first_half[::-1]

    return first_half + middle_char + second_half

# Example usage
nameString = "yxxy"
result = computeEncodedProductName(nameString)
print(result)  # Output should be "xyyx"

# Example usage
nameString = "ded"
result = computeEncodedProductName(nameString)
print(result)  # Output should be "ded"
