import datetime
import pytest
import seasons

def test_dates():
    with pytest.raises(ValueError):
        seasons.get_dates("1998-20-31")
    with pytest.raises(ValueError):
        seasons.get_dates("1998-09-40")
    with pytest.raises(ValueError):
        seasons.get_dates("19-09-40")

# def test_minutes():
#     assert seasons.get_diff(set(1998, 9,14), set(2023, 2, 8)) ==