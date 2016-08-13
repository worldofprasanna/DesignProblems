from .score import score

def test_score_of_an_empty_list_is_zero():
    assert score([]) == 0

def test_score_of_a_single_roll_of_5_is_50():
    assert 50 == score([5])

def test_score_of_a_single_roll_of_1_is_100():
    assert 100 == score([1])
