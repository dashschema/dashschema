from typing import List, Literal, Union
from pydantic import BaseModel, Field

from .base import BaseWidget

Formatter = Literal["number", "currency", "date", "percent"]


class TableColumn(BaseModel):
    name: str = Field(..., description="Column name")
    data_key: str = Field(..., description="Data key to use for this column")
    data_type: Literal["string", "number", "date", "currency"] = Field(
        description="Data type of the column", default="string"
    )
    data_formatters: List[Formatter] = Field(
        description="Data formatters to apply to the column", default_factory=list
    )
    align: Literal["left", "center", "right"] = Field(
        description="Alignment of the column", default="left"
    )


class TableDataPoint(BaseModel):
    value: Union[int, float, str] = Field(..., description="Value of the data point")


class TableData(BaseModel):
    columns: List[TableColumn]
    rows: List[dict[str, TableDataPoint]]


class TableWidget(BaseWidget):
    type: Literal["table"]
    data: TableData = Field(..., description="Widget data")

    @classmethod
    def examples(cls):
        return [
            cls(
                **{
                    "type": "table",
                    "data": {
                        "columns": [
                            {
                                "name": "Name",
                                "data_key": "name",
                                "data_type": "string",
                                "data_formatters": [],
                                "align": "left",
                            },
                            {
                                "name": "Age",
                                "data_key": "age",
                                "data_type": "number",
                                "data_formatters": ["number"],
                                "align": "right",
                            },
                        ],
                        "rows": [
                            {"name": {"value": "Alice"}, "age": {"value": 25}},
                            {"name": {"value": "Bob"}, "age": {"value": 30}},
                        ],
                    },
                }
            ),
            cls(
                title="Table Example",
                description="This is an example of a table",
                **{
                    "type": "table",
                    "data": {
                        "columns": [
                            {
                                "name": "Name",
                                "data_key": "name",
                                "data_type": "string",
                                "data_formatters": [],
                                "align": "left",
                            },
                            {
                                "name": "Age",
                                "data_key": "age",
                                "data_type": "number",
                                "data_formatters": ["number"],
                                "align": "right",
                            },
                        ],
                        "rows": [
                            {"name": {"value": "Alice"}, "age": {"value": 25}},
                            {"name": {"value": "Bob"}, "age": {"value": 30}},
                        ],
                    },
                }
            ),
        ]

    @staticmethod
    def doc():
        return """
Use a table to display tabular data, with optional sorting and formatting.
"""
