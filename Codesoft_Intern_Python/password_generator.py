import random
import string

def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    all_chars = letters + digits + special_chars
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    try:
        password_length = int(input("Enter the desired length of the password: "))
        if password_length <= 0:
            raise ValueError("Password length must be a positive integer.")
    except ValueError as e:
        print(e)
        return
    
    password = generate_password(password_length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
