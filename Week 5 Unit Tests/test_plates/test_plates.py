#no need to use main because pytest takes care of it as long as u start check funtions with test


from plates import is_valid

#“All vanity plates must start with at least two letters.”
def test_starting():
    assert is_valid("CS50")==True
    assert is_valid("P3000")==False

#“Numbers cannot be used in the middle of a plate; they must come at the end.
#For example, AAA222 would be an acceptable; AAA22A would not be acceptable.
#The first number used cannot be a ‘0’.”
def test_num_placement():
    assert is_valid("CS50")==True
    assert is_valid("CS50P")==False
    assert is_valid("50CS")==False
    assert is_valid("50")==False
    assert is_valid("CS05")==False


#vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
def test_num_char():
    assert is_valid("rihab50")==False
    assert is_valid("C")==False

#“No periods, spaces, or punctuation marks are allowed.”
def test_special_char():
    assert is_valid("?!&!?") == False
    assert is_valid(" CS50 ") == False
    assert is_valid("PI3.14") == False