import pytest

from ..src.FizzBuzz import FizzBuzz


@pytest.fixture()
def 前準備():
    global fizz_buzz
    fizz_buzz = FizzBuzz()
    yield fizz_buzz


class TestFizzBuzz(object):
    class Test_convertメソッドは数を文字列に変換する(object):
        class Test_3の倍数のときは数の代わりにFizzに変換する(object):
            def test_3を渡すと文字列Fizzを返す(self, 前準備):
                assert fizz_buzz.convert(3) == 'Fizz'

        class Test_5の倍数のときは数の代わりにBuzzに変換する(object):
            def test_5を渡すと文字列Buzzを返す(self, 前準備):
                assert fizz_buzz.convert(5) == 'Buzz'

        class Test_3と5両方の倍数のときは数の代わりにFizzBuzzに変換する(object):
            def test_15を渡すと文字列FizzBuzzを返す(self, 前準備):
                assert fizz_buzz.convert(15) == 'FizzBuzz'

        class Test_その他の数の時はそのまま文字列に変換する(object):

            def test_1を渡すと文字列1を返す(self, 前準備):
                assert fizz_buzz.convert(1) == '1'

            def test_2を渡すと文字列2を返す(self, 前準備):
                assert fizz_buzz.convert(2) == '2'



if __name__ == '__main__':
    pytest.main()
