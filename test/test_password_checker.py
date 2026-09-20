from password_checker import check_password_strength

def test_short_password():
    assert check_password_strength("abc") == "weak"

def test_long_password():
    assert check_password_strength("abcdefghi") == "strong"