# Example of a test module in pytest

from codewars.tester_function import total


def test_total_empty() -> None:
    #first test - total of empty list should be zero
    assert total([]) == 0.0 
    # uses the boolean value to indicate if a test passes or not

def test_total_single_item() -> None:
    #Total of a single item list should be the item's value
    assert total([110.0]) == 110.0 

def test_total_many_items() -> None:
    #Total of a list with many items should be their sum
    assert total([1.0, 2.0, 3.0]) == 6.0 