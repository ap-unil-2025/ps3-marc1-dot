"""
Bonus Challenge: Password Generator
Generate secure passwords with customizable options.
"""

import random
import string


def generate_password(length=12, use_uppercase=True, use_lowercase=True,
                     use_digits=True, use_special=True):
    """
    Generate a random password based on criteria.

    Args:
        length (int): Length of the password
        use_uppercase (bool): Include uppercase letters
        use_lowercase (bool): Include lowercase letters
        use_digits (bool): Include digits
        use_special (bool): Include special characters

    Returns:
        str: Generated password
    """
    characters = ""

    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return "Error: No character types selected!"

    password = []

   # Ensure at least one character from each selected type
    if use_lowercase:
        password.append(random.choice(string.ascii_lowercase))
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))

    # Fill the rest randomly
    while len(password) < length:
        password.append(random.choice(characters))

    # Shuffle the list to randomize order
    random.shuffle(password)
    
    return ''.join(password)


def password_strength(password):
    """
    Rate password strength from 1-5.

    Args:
        password (str): Password to evaluate

    Returns:
        str: Strength rating
    """
    score = 0

    # TODO: Add points for different criteria
    # - Length >= 8: +1 point
    # - Length >= 12: +1 point
    # - Contains lowercase: +1 point
    # - Contains uppercase: +1 point
    # - Contains digits: +1 point

    strength = ["Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"]
    return strength[min(score, 5)]


def main():
    """Main function to run the password generator."""
    print("Password Generator")
    print("-" * 30)

    # Get password length from user
    length_input = input("Password length (default 12): ").strip()
    length = int(length_input) if length_input else 12

    # Generate password
    password = generate_password(length)
    print(f"\nGenerated Password: {password}")
    print(f"Strength: {password_strength(password)}")

    # Generate alternative passwords
    print("\nAlternative passwords:")
    for i in range(3):
        alt_password = generate_password(length)
        print(f"{i+1}. {alt_password} ({password_strength(alt_password)})")


if __name__ == "__main__":
    main()