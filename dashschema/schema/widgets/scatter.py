from typing import List, Literal
from pydantic import BaseModel, Field

from dashschema.schema.series import ContinuousPoint

from .base import BaseWidget


class ScatterDataPoint(BaseModel):
    x: ContinuousPoint
    y: ContinuousPoint


class ScatterChartSeries(BaseModel):
    label: str = Field(..., description="Series label")
    points: List[ScatterDataPoint] = Field(..., description="Series data")


class ScatterChartWidget(BaseWidget):
    type: Literal["scatter-chart"]
    data: List[ScatterChartSeries] = Field(..., description="Widget data")


    @classmethod
    def examples(cls):
        return [
            cls(
                **{
                    "type": "scatter-chart",
                    "data": [
                        {"label": "A", "points": [{"x": 1, "y": 10}, {"x": 2, "y": 20}, {"x": 3, "y": 25}]},
                        {"label": "B", "points": [{"x": 1.2, "y": 15}, {"x": 2.8, "y": 25}, {"x": 3.14, "y": 30}]},
                    ],
                }
            ),
            cls(
                title="Scatter Chart Example",
                description="This is an example of a scatter chart",
                **{
                    "type": "scatter-chart",
                    "data": [
                        {"label": "A", "points": [{"x": 1, "y": 10}, {"x": 2, "y": 20}, {"x": 3, "y": 15}]},
                        {"label": "B", "points": [{"x": 1.5, "y": 15}, {"x": 2.2, "y": 25}, {"x": 3, "y": 30}]},
                    ],
                }
            ),
        ]
    
    @staticmethod
    def doc():
        return """
Use a scatter chart to display a series of points, each with a label and a series of points. X and Y values are continuous.
"""
