import string

password = input("Enter Password: ")

score = 0

# Checking conditions

if len(password) >= 8:
    score += 1

if any(c.isupper() for c in password):
    score += 1

if any(c.islower() for c in password):
    score += 1

if any(c.isdigit() for c in password):
    score += 1

if any(c in string.punctuation for c in password):
    score += 1


# Strength

if score <= 2:
    print("\nStrength: WEAK")

elif score == 3:
    print("\nStrength: MEDIUM")

elif score == 4:
    print("\nStrength: STRONG")

else:
    print("\nStrength: VERY STRONG")


# Vulnerability Analysis

print("\nVulnerabilities:")

if len(password) < 8:
    print("- Password too short")

if password.isnumeric():
    print("- Only numbers used")
    print("- Easy to guess")
    print("- Easy to brute force")

if password.isalpha():
    print("- Only letters used")

if password.lower() == password:
    print("- No uppercase letters")

if password.upper() == password:
    print("- No lowercase letters")

if not any(c in string.punctuation for c in password):
    print("- No special characters")

if score == 5:
    print("- No vulnerabilities found")