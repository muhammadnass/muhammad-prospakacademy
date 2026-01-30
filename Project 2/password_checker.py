#The code validates a password based on specific security criteria.

def main():
    password = input("Enter your password: ")

    #Flags initialization
    has_min_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False

    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    if len(password) >= 8:
        has_min_length = True

    #Looping to check character types
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

        if all([has_min_length, has_uppercase, has_lowercase, has_digit, has_special]):
            break

    #list storing error messages
    feedback_messages = []

    if not has_min_length:
        feedback_messages.append("Password must be at least 8 characters long.")
    if not has_uppercase:
        feedback_messages.append("Password must contain at least one uppercase letter.")
    if not has_lowercase:
        feedback_messages.append("Password must contain at least one lowercase letter.")
    if not has_digit:
        feedback_messages.append("Password must contain at least one digit.")
    if not has_special:
        feedback_messages.append("Password must contain at least one special character.")

    #overall status checking and printing
    if not feedback_messages:
        print("Password is strong!")
    else:
        print("Password needs improvement:")
        for message in feedback_messages:
            print(f"- {message}")

if __name__ == "__main__":
    main()