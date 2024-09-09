import secrets
import string

def get_user_input():
    """
    Prompt the user for password requirements and return these options.
    """
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                raise ValueError("Password length must be at least 1.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive integer.")

    include_uppercase = get_boolean_input("Include uppercase letters? (y/n): ")
    include_digits = get_boolean_input("Include digits? (y/n): ")
    include_special = get_boolean_input("Include special characters? (y/n): ")

    return length, include_uppercase, include_digits, include_special

def get_boolean_input(prompt):
    """
    Get a boolean input ('y' or 'n') from the user.
    """
    while True:
        response = input(prompt).strip().lower()
        if response in ['y', 'n']:
            return response == 'y'
        print("Invalid input. Please enter 'y' or 'n'.")

def generate_password(length, include_uppercase, include_digits, include_special):
    """
    Generate a secure password with specified length and character set options.

    Args:
        length (int): Length of the generated password.
        include_uppercase (bool): Whether to include uppercase letters.
        include_digits (bool): Whether to include digits.
        include_special (bool): Whether to include special characters.

    Returns:
        str: The generated password.
    """
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits if include_digits else ''
    special = string.punctuation if include_special else ''

    alphabet = lowercase + uppercase + digits + special

    
    if not alphabet:
        raise ValueError("At least one character set must be included.")

    
    password = []
    if include_uppercase:
        password.append(secrets.choice(uppercase))
    if include_digits:
        password.append(secrets.choice(digits))
    if include_special:
        password.append(secrets.choice(special))

    
    if length > len(password):
        password += [secrets.choice(alphabet) for _ in range(length - len(password))]

    
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

def main():
    length, include_uppercase, include_digits, include_special = get_user_input()
    password = generate_password(length, include_uppercase, include_digits, include_special)
    print(f"Generated Password: {password}")

if __name__ == "_main_":
    main()