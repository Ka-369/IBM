user_credintials = [
    ("user1", "pass1"),
    ("user2", "pass2"),
    ("user3", "pass3")
]

username = input("Enter your username: ")
password = input("Enter your password: ")

if (username, password) in user_credintials:
    print("Login successful!")
else:
    print("Invalid username or password.")
    
