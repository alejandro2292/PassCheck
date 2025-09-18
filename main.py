
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



if __name__ == "__main__":  

    password = input('Enter your password : ') #Password recovery
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



print(score)

