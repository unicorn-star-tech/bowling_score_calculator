from application.bowling_model import BowlingGameLogic


def test_strike_score__bad():
    model = BowlingGameLogic()
    model.throws = [0] * 21
    assert model.score(9) == 0


def test_strike_score__perfect():
    model = BowlingGameLogic()
    model.throws = [10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 10, 10]
    assert model.score(9) == 300
