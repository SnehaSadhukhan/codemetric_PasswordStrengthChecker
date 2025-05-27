import re

def check_password_strength(password):
    suggestions = []
    score = 0

    if len(password) < 8:
        suggestions.append("At least 8 characters required.")
    else:
        score += 1

    if not re.search(r'[A-Z]', password):
        suggestions.append("Include at least one uppercase letter.")
    else:
        score += 1

    if not re.search(r'[a-z]', password):
        suggestions.append("Include at least one lowercase letter.")
    else:
        score += 1

    if not re.search(r'\d', password):
        suggestions.append("Include at least one number.")
    else:
        score += 1

    if not re.search(r'[!@#$%^&*(){}\[\]:;<>,.?/~_+\-=|\\]', password):
        suggestions.append("Include at least one special character.")
    else:
        score += 1

    if score == 5:
        return "Strong: Your password is secure!"
    elif score >= 3:
        return "Moderate: Improve your password with the following suggestions:\n" + "\n".join(suggestions)
    else:
        return "Weak: Consider the following improvements:\n" + "\n".join(suggestions)

def password_checker():
    print("🔐 Welcome to the Password Strength Checker\n")

    while True:
        password = input("Enter your password (or type 'exit' to quit): ")

        if password.lower() == 'exit':
            print(" Thank you for using the tool!")
            break

        result = check_password_strength(password)
        print("\n" + result + "\n")

if __name__ == "__main__":
    password_checker()
