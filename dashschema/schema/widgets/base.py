from typing import Optional, Literal
from pydantic import BaseModel, Field


class BaseWidget(BaseModel):
    type: Literal["widget"]
    id: str = Field(description="Widget ID", default="")
    title: str = Field(description="Widget title", default="", max_length=100)
    description: str = Field(description="Widget description", default="", max_length=500)

    x: int = Field(description="Widget x position", default=-1)
    y: int = Field(description="Widget y position", default=-1)
    row: int = Field(description="Widget row position", default=-1)
    col: int = Field(description="Widget col position", default=-1)


    @classmethod
    def widget_name(cls):
        # Human readable name of widget. eg; BarChartWidget -> "Bar chart"
        base_name = cls.__name__.replace("Widget", "")
        res = []
        start = 0
        for i, c in enumerate(base_name[1:], 1):
            if c.isupper():
                res.append(base_name[start:i])
                start = i
        res.append(base_name[start:])
        return " ".join(res)

    def __str__(self):
        super_str = super().__str__()
        return f"<{self.widget_name()} {super_str}>"