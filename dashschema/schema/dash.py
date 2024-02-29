from datetime import datetime
from typing import Union, get_args
from pydantic import BaseModel, Field, root_validator

from .widgets.table import TableWidget
from .widgets.pie import PieChartWidget
from .widgets.bar import BarChartWidget
from .widgets.line import LineChartWidget
from .widgets.scatter import ScatterChartWidget
from .widgets.metric import MetricWidget
from .widgets.inputs import (
    DateSelectWidget,
    DateRangeSelectWidget,
    SearchWidget,
    SingleSelectWidget,
    MultiSelectWidget,
)
from .widgets.layout import TitleWidget, DescriptionWidget, HorizontalRulerWidget, VerticalRulerWidget  

FilterWidget = Union[
    DateSelectWidget,
    DateRangeSelectWidget,
    SearchWidget,
    SingleSelectWidget,
    MultiSelectWidget,
]

DataWidget = Union[
    MetricWidget,
    BarChartWidget,
    TableWidget,
    PieChartWidget,
    LineChartWidget,
    ScatterChartWidget,
]

LayoutWidget = Union[TitleWidget, DescriptionWidget, HorizontalRulerWidget, VerticalRulerWidget]

Widget = Union[FilterWidget, DataWidget, LayoutWidget]

WIDGETS = list(DataWidget.__args__) + list(FilterWidget.__args__) + list(LayoutWidget.__args__)

TYPE_TO_WIDGET: dict[str, Widget] = {
    get_args(kls.model_fields["type"].annotation)[0]: kls for kls in WIDGETS
}


class Dashboard(BaseModel):
    version: str = Field(description="Schema version", default="0.0.1")
    generated_at: datetime = Field(
        ..., description="Dashboard generation time", default_factory=datetime.now
    )

    widgets: list[Widget] = Field(..., description="Dashboard widgets")

    @root_validator(pre=True)
    def create_widgets(cls, values):
        return {
            **values,
            "widgets": [TYPE_TO_WIDGET[w["type"]](**w) for w in values["widgets"]],
        }
