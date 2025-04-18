import pytest

from codetiming import fTimer, Timer


@fTimer(logger=None)
def decorated_function(num: int = 1000):
    sum(n**2 for n in range(num))


def test_ftimer():
    decorated_function()
    print(Timer.timers)
    assert "decorated_function" in Timer.timers


if __name__ == "__main__":
    pytest.main([__file__])
