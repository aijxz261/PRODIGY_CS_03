import string

def assess_password(password: str) -> dict:
    """Return strength and feedback for a given password."""
    feedback = []

    # Criteria checks
    length_ok = len(password) >= 8
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    # Build score
    score = 0
    if length_ok:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if has_lower:
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if has_upper:
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if has_digit:
        score += 1
    else:
        feedback.append("Add at least one number.")

    if has_special:
        score += 1
    else:
        feedback.append("Add at least one special character (e.g. !, @, #, ?).")

    # Map score to strength label
    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return {
        "strength": strength,
        "score": score,
        "feedback": feedback if feedback else ["Good job! Your password looks strong."]
    }

# Simple CLI usage
if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    result = assess_password(pwd)

    print(f"\nPassword strength: {result['strength']} ({result['score']}/5)")
    print("Feedback:")
    for msg in result["feedback"]:
        print(f"- {msg}")