from twttr import shorten

def main():
    test_cases()
    test_numbers()
    test_characters()

#test implementation of shorten
def test_cases():
    assert shorten("twitter")=="twttr"
    assert shorten("TWITTER")=="TWTTR"
    assert shorten("twItTeR")=="twtTR"
def test_numbers():
    assert shorten("50")=="50"
def test_characters():
    assert shorten("snap!!!!")=="snp!!!!"

if __name__ == "__main__":
    main()