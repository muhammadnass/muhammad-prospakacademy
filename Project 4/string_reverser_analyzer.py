"""
Lab 5.2: String Reverser and Analyzer
This script takes user input, reverses it, counts vowels and consonants, 
and determines if the input is a palindrome.
"""

def reverse_string(text):
    """
    Returns the input text reversed using string slicing.
    """
    return text[::-1]


def count_vowels_consonants(text):
    """
    Counts vowels and consonants in the string, ignoring non-alphabetic characters.
    """
    # Convert to lowercase to simplify comparisons
    text = text.lower()
    vowel_count = 0
    consonant_count = 0
    vowels = "aeiou"

    for char in text:
        # Check if the character is an alphabet letter
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
                
    return vowel_count, consonant_count


def is_palindrome(text):
    """
    Checks if a string is a palindrome by cleaning it of spaces/punctuation
    and comparing it to its reversed version.
    """
    # Clean the text: lowercase and keep only alphanumeric characters
    cleaned_text = "".join(char.lower() for char in text if char.isalnum())
    
    # Compare cleaned text with its reversed version
    return cleaned_text == cleaned_text[::-1]


def main():
    # Prompt the user to enter a phrase
    phrase = input("Enter a phrase: ")
    
    # Perform string reversal
    reversed_phrase = reverse_string(phrase)
    print(f"Reversed phrase: {reversed_phrase}")
    
    # Perform vowel and consonant counting
    v_count, c_count = count_vowels_consonants(phrase)
    print(f"Vowels: {v_count}, Consonants: {c_count}")
    
    # Check if the phrase is a palindrome
    palindrome_status = is_palindrome(phrase)
    print(f"Is it a palindrome? {palindrome_status}")


if __name__ == "__main__":
    main()