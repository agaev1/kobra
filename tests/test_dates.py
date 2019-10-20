from kobra import Date_custom
import QuantLib as ql


def test_date_returns_quantlib():
    result = Date_custom('2019-10-01')
    result = result.quantlib

    compare_to = ql.Date(1, 10, 2019)

    assert result == compare_to
