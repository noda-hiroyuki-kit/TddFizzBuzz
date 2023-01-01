import pytest

from ..src.FizzBuzz import FizzBuzz


class TestFizzBuzz(object):
    def test_1を渡すと文字列1を返す(self):
        # 準備
        fizz_buzz = FizzBuzz()
        # 実行 & 検証
        assert fizz_buzz.convert(1) == '1'


if __name__ == '__main__':
    pytest.main()
