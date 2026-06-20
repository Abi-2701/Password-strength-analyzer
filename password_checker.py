import re

password = input("Enter Password: ")

score = 0

if len(password) >= 8:
    score += 1

if re.search(r"[A-Z]", password):
    score += 1

if re.search(r"[a-z]", password):
    score += 1

if re.search(r"\d", password):
    score += 1

if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1

print("\nPassword Analysis")
print("-" * 30)

if score <= 2:
    print("Strength: Weak")
elif score <= 4:
    print("Strength: Medium")
else:
    print("Strength: Strong")

print(f"Security Score: {score}/5")

if score < 5:
    print("\nRecommendations:")
    
    if len(password) < 8:
        print("- Use at least 8 characters")
        
    if not re.search(r"[A-Z]", password):
        print("- Add uppercase letters")
        
    if not re.search(r"[a-z]", password):
        print("- Add lowercase letters")
        
    if not re.search(r"\d", password):
        print("- Add numbers")
        
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("- Add special characters")
