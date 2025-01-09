from um import count

def main():
    test_case()
    test_um_in_word()
    test_space()

def test_case():
    assert count("Um, thanks for the album")==1
    assert count("Um, thanks, um")==2

def test_um_in_word():
    assert count("yummi")==0
    assert count("mum")==0

def test_space():
    assert count("hello um rihab !")==1
    assert count("um?")==1

