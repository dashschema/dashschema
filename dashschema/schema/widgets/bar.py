from typing import List, Optional, Union, Literal
from pydantic import BaseModel, Field

from dashschema.schema.series import ContinuousPoint, DiscretePoint
from dashschema.schema.behaviors import OnPressBehavior

from .base import BaseWidget


class BarDataPoint(BaseModel):
    x: Union[DiscretePoint]
    y: ContinuousPoint
    # onpress: OnPressBehavior = Field(description="On press behavior", default=lambda: OnPressBehavior())


class BarChartWidget(BaseWidget):
    type: Literal["bar-chart"]
    bars: List[BarDataPoint] = Field(..., description="Widget data")

    @classmethod
    def examples(cls):
        return [
            cls(
                **{
                    "type": "bar-chart",
                    "bars": [
                        {"x": "A", "y": 10},
                        {"x": "B", "y": 20},
                        {"x": "C", "y": 25},
                    ],
                }
            ),
            cls(
                title="Bar Chart Example",
                description="This is an example of a bar chart",
                **{
                    "type": "bar-chart",
                    "bars": [
                        {"x": "A", "y": 10},
                        {"x": "B", "y": 20},
                        {"x": "C", "y": 15},
                    ],
                }
            ),
        ]

    @staticmethod
    def doc():
        return """
Use a bar chart to display a series of bars, each with a discrete x value and a continuous y value.
Bar charts work best when the y value represents a count or a sum, and the x value represents a category or a time period.
Y values should be positive, and the x values should be unique.
"""
