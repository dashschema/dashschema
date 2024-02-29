from typing import List, Union, Literal
from pydantic import BaseModel, Field

from dashschema.schema.series import ContinuousPoint, DiscretePoint

from .base import BaseWidget


class LineDataPoint(BaseModel):
    x: Union[ContinuousPoint, DiscretePoint]
    y: ContinuousPoint


class LineChartSeries(BaseModel):
    label: str = Field(..., description="Series label")
    points: List[LineDataPoint] = Field(..., description="Series data")


class LineChartWidget(BaseWidget):
    type: Literal["line-chart"]
    data: list[LineChartSeries] = Field(description="Widget data")

    @classmethod
    def examples(cls):
        return [
            cls(
                **{
                    "type": "line-chart",
                    "data": [
                        {"label": "A", "points": [{"x": "A", "y": 10}, {"x": "B", "y": 20}, {"x": "C", "y": 25}]},
                        {"label": "B", "points": [{"x": "A", "y": 15}, {"x": "B", "y": 25}, {"x": "C", "y": 30}]},
                    ],
                }
            ),
            cls(
                title="Line Chart Example",
                description="This is an example of a line chart",
                **{
                    "type": "line-chart",
                    "data": [
                        {"label": "A", "points": [{"x": "A", "y": 10}, {"x": "B", "y": 20}, {"x": "C", "y": 15}]},
                        {"label": "B", "points": [{"x": "A", "y": 15}, {"x": "B", "y": 25}, {"x": "C", "y": 30}]},
                    ],
                }
            ),
            cls(
                title="Line Chart Example",
                description="This is an example of a line chart",
                **{
                    "type": "line-chart",
                    "data": [
                        {"label": "A", "points": [{"x": 1, "y": 10}, {"x": 3, "y": 20}, {"x": 7, "y": 15}]},
                        {"label": "B", "points": [{"x": 2, "y": 15}, {"x": 3, "y": 25}, {"x": 5, "y": 30}]},
                    ],
                }
            ),
        ]

    @staticmethod
    def doc():
        return """
Use a line chart to display a series of lines, each with a label and a series of points. X values can be either continuous or discrete.
Prefer line charts to scatter charts when values between points are assumed to be interpolated.
"""
