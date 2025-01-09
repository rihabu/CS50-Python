from bank import value

def main():
    test_value_0()
    test_value_20()
    test_value_100()

def test_value_0():
    assert value("hello")==0 and value("Hello")==0

def test_value_20():
    assert value("Hi")==20 and value("hey")==20

def test_value_100():
    assert value("Yo!")==100 and value("greetings")==100
    
if __name__ == "__main__":
    main()