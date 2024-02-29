from typing import List, Optional, Literal
from pydantic import BaseModel, Field

from dashschema.schema.series import ContinuousPoint
from dashschema.schema.behaviors import OnPressBehavior

from .base import BaseWidget


class PieChartDataPoint(BaseModel):
    label: str
    value: ContinuousPoint


class PieChartWidget(BaseWidget):
    type: Literal["pie-chart"]
    slices: List[PieChartDataPoint] = Field(..., description="Widget data")

    @classmethod
    def examples(cls) -> List["PieChartWidget"]:
        return [
            cls(
                **{
                    "type": "pie-chart",
                    "slices": [
                        {"label": "A", "value": 10},
                        {"label": "B", "value": 20},
                        {"label": "C", "value": 25},
                    ],
                }
            ),
            cls(
                title="Pie Chart Example",
                description="This is an example of a pie chart",
                **{
                    "type": "pie-chart",
                    "slices": [
                        {"label": "A", "value": 10},
                        {"label": "B", "value": 20},
                        {"label": "C", "value": 15},
                    ],
                }
            ),
        ]

    @staticmethod
    def doc() -> str:
        return """
Use a pie chart to display a series of slices, each with a label and a value. Values must be postive. For best results, a pie chart should have at most 5 slices.
"""