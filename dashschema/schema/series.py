import re

# Data series schema
from typing import Union
from typing_extensions import Annotated
from pydantic import AfterValidator

ContinuousPoint = float

# Ints can be discrete, eg years or zipcodes
DiscretePoint = Union[str, int]

# Date buckets
year_regex = re.compile(r"^\d{4}$")


def is_year(s: DiscretePoint) -> bool:
    if isinstance(s, str):
        assert year_regex.match(s) is not None
    elif isinstance(s, int):
        assert s >= 0 and s <= 9999
    return s


def validate_regex(regex: re.Pattern) -> AfterValidator:
    def validate(s: str) -> bool:
        assert regex.match(s) is not None
        return s

    return AfterValidator(validate)


YearBucket = Annotated[str, AfterValidator(is_year)]

month_regex = re.compile(r"^\d{4}-\d{2}$")
MonthBucket = Annotated[str, validate_regex(month_regex)]

day_regex = re.compile(r"^\d{4}-\d{2}-\d{2}$")
DayBucket = Annotated[str, validate_regex(day_regex)]

week_regex = re.compile(r"^\d{4}-W\d{2}$")
WeekBucket = Annotated[str, validate_regex(week_regex)]

hour_regex = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}$")
HourBucket = Annotated[str, validate_regex(hour_regex)]

minute_regex = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}$")
MinuteBucket = Annotated[str, validate_regex(minute_regex)]


DateBucket = Union[
    YearBucket, MonthBucket, DayBucket, WeekBucket, HourBucket, MinuteBucket
]
