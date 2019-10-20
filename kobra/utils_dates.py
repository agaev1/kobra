import QuantLib as ql
from datetime import datetime
from kobra.enums_currencies import Currencies


class Date_custom:

    def __init__(self, date_string='2018-01-01'):
        self.date_string = date_string

    @staticmethod
    def string_to_datetime(d):
        return datetime.strptime(d, "%Y-%m-%d")

    @staticmethod
    def string_to_quantlib(d):
        return ql.DateParser.parseFormatted(d, '%Y-%m-%d')

    @staticmethod
    def quantlib_to_datetime(d):
        return datetime(d.year(), d.month(), d.dayOfMonth())

    @staticmethod
    def datetime_to_quantlib(d):
        return ql.DateParser.parseFormatted(d.strftime('%Y-%m-%d'), '%Y-%m-%d')

    @staticmethod
    def datetime_to_string(d):
        return d.strftime('%Y-%m-%d')

    # Properties
    @property
    def string(self):
        return self.date_string

    @property
    def datetime(self):
        return self.string_to_datetime(self.date_string)

    @property
    def date(self):
        return self.string_to_datetime(self.date_string).date()

    @property
    def quantlib(self):
        return self.string_to_quantlib(self.date_string)

    # Regular functions
    def two_days_in_center(self, currency_pair='USDNOK', center=None):

        if center is None:
            center_currency = Currencies[currency_pair[-3:]]
            foreign_currency = Currencies[currency_pair[:3]]
        else:
            if center == currency_pair[:3] or center == currency_pair[-3:]:
                center_currency = Currencies[center]
                foreign_currency = Currencies[currency_pair.replace(center, '')]
            else:
                raise ValueError('Center was not in the currency pair.')

        joint_calendar = ql.JointCalendar(foreign_currency.calendar, center_currency.calendar)

        two_center = center_currency.calendar.advance(self.quantlib, ql.Period(2, ql.Days))

        if foreign_currency.calendar.isBusinessDay(two_center):
            spot = two_center
        else:
            spot = joint_calendar.advance(self.quantlib, ql.Period(2, ql.Days))

        return spot

    # Class methods as alternative constructors
    @classmethod
    def from_quantlib(cls, quantlib_date):
        date_datetime = cls.quantlib_to_datetime(quantlib_date)
        date_string = cls.datetime_to_string(date_datetime)
        return cls(date_string)

    @classmethod
    def from_datetime(cls, datetime_date):
        date_string = cls.datetime_to_string(datetime_date)
        return cls(date_string)
