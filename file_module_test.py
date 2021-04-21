from file_module import fizzBuzz


def test_fizz()-> None:
    assert fizzBuzz([3, 6, 9]) == 'Fizz'

def test_fizzBuzz()-> None:
    assert fizzBuzz([15, 30, 45]) == 'FizzBuzz'

def test_fizzBuzzDong()-> None:
    assert fizzBuzz([45, 90, 180]) == 'FizzBuzzDong'

