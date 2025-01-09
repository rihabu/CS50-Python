from numb3rs import validate

def main():
    test_format()
    test_numbers()


def test_format():
    assert validate(r"1.2.3.4")==True
    assert validate(r"1.2.4")==False
    assert validate(r"1.0.0.1")==True
    assert validate(r"1.1")==False

def test_numbers():
    assert validate(r"1.255.255.255")==True
    assert validate(r"512.1.1.1")==False
    assert validate(r"1.512.1.1")==False
    assert validate(r"1.1.1.512")==False

