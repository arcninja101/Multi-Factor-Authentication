user_password_mapping = {
        "Samyukta": "password0",
        "Aryan": "password1",
        "Shivangi": "password3",
        "Vinithra": "password4",
        # Add more users as needed
    }
def verify_password(username, password):
    # Verify password for the given username
    if username in user_password_mapping:
        if user_password_mapping[username] == password:
            return True
    return False
