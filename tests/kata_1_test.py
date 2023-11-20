from codewars.kata_1 import alphabet_position

def test_alphabet_position_word() -> None:
    #first test - test one word
    assert alphabet_position("Cat") == "3 1 20" 

def test_alphabet_position_nonletters() -> None:
    #first test - ignore all non-letters
    assert alphabet_position("12'.a") == "1" 

def test_alphabet_position_sentence() -> None:
    #Test a sentence
    assert alphabet_position("The sunset sets at twelve o clock") == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"