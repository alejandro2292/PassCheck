
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
    special_char = "!@#$%^&*()-_=+[]{};:,<.>/?\\|`~"
    return any(c in special_char for c in password)



if __name__ == "__main__":  

    password = input('Enter your password : ') #Password recovery

    #Print password analysis for the user
    print("\nPassword analysis : ")
    print(f"Contains uppercase letter ? {has_upper(password)}")
    print(f"Contains lower letter ? {has_lower(password)}")
    print(f"Contains digit ? {has_digit(password)}")
    print(f"Contains special character ? {has_special(password)}")



