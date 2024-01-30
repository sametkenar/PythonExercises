def is_palindrome(text):
    # Base case: if the length of text is 0 or 1, it's a palindrome
    if len(text) <= 1:
        return True
    
    # Compare the first and last characters
    if text[0] != text[-1]:
        return False
    
    # Recur on the substring between the first and last characters
    return is_palindrome(text[1:-1])

# Example usage

word1 = "onino"
word2 = "onion"

print(is_palindrome(word1))
print(is_palindrome(word2))