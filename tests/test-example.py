import pytest

class TestMathOperations:
    def test_addition(self):
        assert 2 + 2 == 4  # Original test
    
    def test_negative_numbers(self):
        assert -1 + (-2) == -3  # Edge case
    
    def test_large_numbers(self):
        assert 1000000 + 2000000 == 3000000  # Large values

if __name__ == "__main__":
    pytest.main()