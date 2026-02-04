from src.grade import grades

def test_A_plus():
    assert grades(93)=="A+"

def test_A():
    assert grades(78)=="A"

def test_B():
    assert grades(65)=="B"

def test_C():
    assert grades(52)=="C"

def test_Fail():
    assert grades(40)=="Fail"
