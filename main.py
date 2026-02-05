
#Functions to check the presence of different character types

#Check for uppercase letters
def has_upper(password: str) -> bool: 
    return any(c.isupper() for c in password)

#Check for lowercase letters
def has_lower(password: str) -> bool:
    return any(c.islower() for c in password)

#Check for digits
def has_digit(password: str) -> bool:
    return any(c.isdigit() for c in password)

#Check for special characters
def has_special(password: str) -> bool:
    special_char = "!@#€$£%^&*()-_=+[]{};:,<.>/?\\|`~"
    return any(c in special_char for c in password)

#Functions to set up recommandation
def get_recommendations(password: str) -> list:
    suggestions = []
    if not has_upper(password):
        suggestions.append("- Include uppercase letters (A-Z).")
    if not has_lower(password):
        suggestions.append("- Include lowercase letters (a-z).")
    if not has_digit(password):
        suggestions.append("- Add numerical digits (0-9).")
    if not has_special(password):
        suggestions.append("- Use special characters (e.g., !, @, #).")
    if len(password) < 12:
        suggestions.append("- Increase the length (aim for at least 13 characters).")
            
    return suggestions

if __name__ == "__main__":  

    password = input('Enter your password : ') 
    score = 0 #final password strength score

    #Add points for character types in the password
    if has_upper(password):
        score += 1
    if has_lower(password):
        score += 1
    if has_digit(password):
        score += 1
    if has_special(password):
        score += 1

    
    #Add point for password lenght
    if 8 <= len(password) <= 12:
        score += 2
    elif 13 <= len(password) <= 16:
        score += 4
    elif len(password) > 16:
        score += 7


    #Penalize three consecutive identical characters
    for i in range(len(password)-2):
        if password[i] == password[i+1] == password[i+2]:
            score -= 1


    # Evaluate password strength based on the final score
    print("\n" + "-"*30)
    if score <= 3:
        print("You’re asking for your account to get hacked.")
    elif score <= 6:
        print("It’s a good start, but you should make it stronger.")
    elif score <= 10:
        print("Very solid password.")
    else:
        print("What is this password, did you fall asleep on the keyboard?")

    tips = get_recommendations(password)
    
    # We only show tips if the score isn't perfect
    if tips and score < 11:
        print("\nSuggestions to improve your security:")
        for tip in tips:
            print(tip)
    
    print("-"*30)

