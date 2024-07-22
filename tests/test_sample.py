import pytest
from source.sample import Calculator

class TestCalculator:
    def setup_method(self):
        self.calculator = Calculator()

    def test_add(self):
        assert self.calculator.add(1, 2) == 3
        assert self.calculator.add(-1, -1) == -2
        assert self.calculator.add(-1, 1) == 0

    def test_divide(self):
        assert self.calculator.divide(4, 2) == 2
        assert self.calculator.divide(9, 3) == 3
        with pytest.raises(ZeroDivisionError):
            self.calculator.divide(1, 0)

    def test_sub(self):
        assert self.calculator.sub(5, 3) == 2
        assert self.calculator.sub(3, 5) == -2
        assert self.calculator.sub(0, 0) == 0

    def test_multi(self):
        assert self.calculator.multi(2, 3) == 6
        assert self.calculator.multi(-1, 3) == -3
        assert self.calculator.multi(0, 5) == 0

if __name__ == "__main__":
    pytest.main()
