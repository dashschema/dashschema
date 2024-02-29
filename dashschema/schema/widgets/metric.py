from typing import Literal, Optional, Union
from pydantic import BaseModel, Field

from .base import BaseWidget


class MetricData(BaseModel):
    data_type: Literal["number", "currency", "percent"] = Field(
        description="Data type of the metric value", default="number"
    )
    value: Union[float, str] = Field(..., description="Value of the metric to display")
    change: str = Field(
        description="Change in the metric value, eg. +3% or -10", default=""
    )
    sentiment: Literal["positive", "negative", "neutral", ""] = Field(
        description="Sentiment of the metric value, eg. positive, negative, neutral",
        default="",
    )
    currency: str = Field(description="Currency code", default="")


class MetricWidget(BaseWidget):
    type: Literal["metric"]
    data: MetricData = Field(..., description="Widget data")

    @classmethod
    def examples(cls):
        return [
            cls(
                **{
                    "type": "metric",
                    "data": {"data_type": "number", "value": 10},
                }
            ),
            cls(
                title="Metric Example",
                description="This is a currency metric",
                **{
                    "type": "metric",
                    "data": {"data_type": "currency", "value": 1000, "change": "+10%", "currency": "USD"},
                }
            ),
        ]


    @staticmethod
    def doc():
        return """
Use a metric to display a single value, with optional change and sentiment.
"""
