
def check_password_strength(password):
    if len(password) < 6:
        return "weak"
    return "strong"