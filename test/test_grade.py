from src.grade import grades, calculate_average


def test_calculate_average():
    assert calculate_average([80, 90, 70, 60, 100]) == 80


def test_A_plus():
    assert grades(95) == "A+"


def test_A():
    assert grades(80) == "A"


def test_B():
    assert grades(65) == "B"


def test_C():
    assert grades(55) == "C"


def test_fail():
    assert grades(40) == "Fail"


# Boundary Tests

def test_boundary_90():
    assert grades(90) == "A+"


def test_boundary_89():
    assert grades(89) == "A"


def test_boundary_75():
    assert grades(75) == "A"


def test_boundary_74():
    assert grades(74) == "B"


def test_boundary_60():
    assert grades(60) == "B"


def test_boundary_59():
    assert grades(59) == "C"


def test_boundary_50():
    assert grades(50) == "C"


def test_boundary_49():
    assert grades(49) == "Fail"
