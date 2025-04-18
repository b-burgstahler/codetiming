# Third party imports
import pytest

# Codetiming imports
from codetiming import Timer, fTimer


class test_class:
    @fTimer()
    def add(self, a, b):
        return a + b


# @Timer(name="outer", logger=None)
@fTimer(logger=None)
def decorated_function(num: int = 1000):
    sum(n**2 for n in range(num))


def test_naming():
    test = test_class()
    test.add(2**8, 2**10)
    test.add(2**8, 2**10)
    assert "tests.test_ftimer.test_class.add" in Timer.timers
    assert Timer.timers.count("tests.test_ftimer.test_class.add") == 2


def test_ftimer():
    decorated_function()
    assert "tests.test_ftimer.decorated_function" in Timer.timers


if __name__ == "__main__":
    pytest.main([__file__])
