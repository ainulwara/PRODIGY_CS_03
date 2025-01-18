import re

# Set of common passwords for quick lookup
COMMON_PASSWORDS = {
    "password", "123456", "123456789", "qwerty", "abc123", "letmein", "monkey",
    "iloveyou", "admin", "welcome", "12345", "1234", "1q2w3e4r", "password1",
    "qwerty123", "12345678", "sunshine", "princess", "football", "123123",
    "dragon", "passw0rd", "password123", "123321"
}

def assess_password_strength(password):
    """Assess the strength of a password based on multiple criteria."""
    if not password:
        return "Invalid", "Password cannot be empty. Please enter a valid password."

    # Criteria checks
    length_criteria = len(password) >= 8
    upper_case_criteria = bool(re.search(r'[A-Z]', password))
    lower_case_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    common_password_criteria = password in COMMON_PASSWORDS

    # Calculate strength score
    strength_score = sum([
        length_criteria,
        upper_case_criteria,
        lower_case_criteria,
        digit_criteria,
        special_char_criteria
    ])

    # Determine strength and provide feedback
    if common_password_criteria:
        return "Weak", "Your password is too common. Avoid using easily guessable passwords."
    elif strength_score < 3:
        return "Weak", (
            "Your password is weak. Consider using at least 8 characters, "
            "including uppercase and lowercase letters, numbers, and special characters."
        )
    elif strength_score == 3:
        return "Moderate", (
            "Your password is moderate. To strengthen it, include a mix of uppercase letters, "
            "numbers, and special characters."
        )
    else:
        return "Strong", "Your password is strong. Great job!"

def main():
    """Main function to interact with the user."""
    print("Welcome to the Password Strength Checker!")
    print("Ensure your password is secure by meeting the following criteria:")
    print("- At least 8 characters long")
    print("- Contains uppercase and lowercase letters")
    print("- Includes numbers and special characters\n")

    while True:
        # Get password input
        password = input("Enter a password to assess its strength: ").strip()
        strength, feedback = assess_password_strength(password)

        # Display results
        print(f"\nPassword Strength: {strength}")
        print(feedback)

        # Ask if the user wants to try again
        try_again = input("\nDo you want to check another password? (yes/no): ").strip().lower()
        if try_again != 'yes':
            print("\nThank you for using the Password Strength Checker. Stay secure!")
            break

if __name__ == "__main__":
    main()
