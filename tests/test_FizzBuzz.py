import pytest

from ..src.FizzBuzz import FizzBuzz


@pytest.fixture()
def 前準備():
    global fizz_buzz
    fizz_buzz = FizzBuzz()
    yield fizz_buzz


class TestFizzBuzz(object):
    def test_1を渡すと文字列1を返す(self, 前準備):
        assert fizz_buzz.convert(1) == '1'

    def test_2を渡すと文字列2を返す(self, 前準備):
        assert fizz_buzz.convert(2) == '2'

    def test_3を渡すと文字列Fizzを返す(self, 前準備):
        assert fizz_buzz.convert(3) == 'Fizz'

    def test_5を渡すと文字列Buzzを返す(self, 前準備):
        assert fizz_buzz.convert(5) == 'Buzz'


if __name__ == '__main__':
    pytest.main()
