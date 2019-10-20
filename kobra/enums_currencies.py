import enum
import QuantLib as ql


class Norway_custom_calendar(ql.Norway):

    def __init__(self):
        super().__init__()

        for year in (2018, 2119):
            self.addHoliday(ql.Date(24, 12, year))


class Single_currency:
    def __init__(self, name, quantlib_calendar):
        self.name = name
        self.quantlib_calendar = quantlib_calendar


class Currencies(enum.Enum):
    NOK = Single_currency('Norway', Norway_custom_calendar)
    USD = Single_currency('United States', ql.UnitedStates)
    GBP = Single_currency('United Kingdom', ql.UnitedKingdom)
    EUR = Single_currency('Eurozone', ql.TARGET)
    SEK = Single_currency('Sweden', ql.Sweden)

    @property
    def country(self):
        return self.value.name

    @property
    def calendar(self):
        return self.value.quantlib_calendar()
