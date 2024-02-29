from typing import List, Optional, Literal
from pydantic import BaseModel

from .base import BaseWidget, Field


class DateSelectWidget(BaseWidget):
    type: Literal["date-select"]
    initial: str = Field(description="Initial date value", default="")

    @classmethod
    def examples(cls):
        return [
            cls(
                **{
                    "type": "date-select",
                    "initial": "2021-01-01",
                }
            ),
            cls(
                title="Date Select Example",
                description="This is an example of a date select",
                **{
                    "type": "date-select",
                    "initial": "2021-01-01",
                }
            ),
        ]


class DateRangeSelectWidget(BaseWidget):
    type: Literal["date-range-select"]
    initial_start: str = Field(
        description="Initial start date value", default=""
    )
    initial_end: str = Field(
        description="Initial end date value", default=""
    )

    @classmethod
    def examples(cls):
        return [
            cls(
                **{
                    "type": "date-range-select",
                    "initial_start": "2021-01-01",
                    "initial_end": "2021-01-31",
                }
            ),
            cls(
                title="Date Range Select Example",
                description="This is an example of a date range select",
                **{
                    "type": "date-range-select",
                    "initial_start": "2021-01-01",
                    "initial_end": "2021-01-31",
                }
            ),
        ]


class SearchWidget(BaseWidget):
    type: Literal["search"]
    initial: str = Field(description="Initial search value", default="")

    @classmethod
    def examples(cls):
        return [
            cls(
                **{
                    "type": "search",
                    "initial": "search term #1",
                }
            ),
            cls(
                title="Search Example",
                description="This is an example of a search",
                **{
                    "type": "search",
                    "initial": "search term #2",
                }
            ),
        ]


class SelectOption(BaseModel):
    value: str = Field(description="Option value")
    label: str = Field(description="Option label")


class SingleSelectWidget(BaseWidget):
    type: Literal["select-single"]
    options: List[SelectOption] = Field(description="List of options", default=None)
    initial: Optional[SelectOption] = Field(description="Initial value", default=None)

    @classmethod
    def examples(cls):
        return [
            cls(
                **{
                    "type": "select-single",
                    "options": [
                        {"value": "option1", "label": "Option 1"},
                        {"value": "option2", "label": "Option 2"},
                        {"value": "option3", "label": "Option 3"},
                    ],
                    "initial": {"value": "option2", "label": "Option 2"},
                }
            ),
            cls(
                title="Single Select Example",
                description="This is an example of a single select",
                **{
                    "type": "select-single",
                    "options": [
                        {"value": "option1", "label": "Option 1"},
                        {"value": "option2", "label": "Option 2"},
                        {"value": "option3", "label": "Option 3"},
                    ],
                    "initial": {"value": "option2", "label": "Option 2"},
                }
            ),
        ]


class MultiSelectWidget(BaseWidget):
    type: Literal["select-multi"]
    options: List[SelectOption] = Field(description="List of options", default=None)
    initial: Optional[List[SelectOption]] = Field(
        description="Initial value", default=None
    )

    @classmethod
    def examples(cls):
        return [
            cls(
                **{
                    "type": "select-multi",
                    "options": [
                        {"value": "option1", "label": "Option 1"},
                        {"value": "option2", "label": "Option 2"},
                        {"value": "option3", "label": "Option 3"},
                    ],
                    "initial": [
                        {"value": "option1", "label": "Option 1"},
                        {"value": "option2", "label": "Option 2"},
                    ],
                }
            ),
            cls(
                title="Multi Select Example",
                description="This is an example of a multi select",
                **{
                    "type": "select-multi",
                    "options": [
                        {"value": "option1", "label": "Option 1"},
                        {"value": "option2", "label": "Option 2"},
                        {"value": "option3", "label": "Option 3"},
                    ],
                    "initial": [
                        {"value": "option1", "label": "Option 1"},
                        {"value": "option2", "label": "Option 2"},
                    ],
                }
            ),
        ]
